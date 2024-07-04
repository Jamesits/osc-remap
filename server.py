from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.udp_client import SimpleUDPClient
from pythonosc.dispatcher import Dispatcher
import asyncio
import math

# listener
server_ip = "::"
server_port = 7002
# dearVR Spatial Connect
upstream_ip = "127.0.0.1"
upstream_port = 7001

quaternion = [0., 0., 0., 0.]

# https://automaticaddison.com/how-to-convert-a-quaternion-into-euler-angles-in-python/
def euler_from_quaternion(x, y, z, w):
        """
        Convert a quaternion into euler angles (roll, pitch, yaw)
        roll is rotation around x in radians (counterclockwise)
        pitch is rotation around y in radians (counterclockwise)
        yaw is rotation around z in radians (counterclockwise)
        """
        t0 = +2.0 * (w * x + y * z)
        t1 = +1.0 - 2.0 * (x * x + y * y)
        roll_x = math.atan2(t0, t1)

        t2 = +2.0 * (w * y - z * x)
        t2 = +1.0 if t2 > +1.0 else t2
        t2 = -1.0 if t2 < -1.0 else t2
        pitch_y = math.asin(t2)

        t3 = +2.0 * (w * z + x * y)
        t4 = +1.0 - 2.0 * (y * y + z * z)
        yaw_z = math.atan2(t3, t4)

        return roll_x, pitch_y, yaw_z # in radians


client = SimpleUDPClient(upstream_ip, upstream_port)

dispatcher = Dispatcher()
def default_handler(address, *args):
    print(f"RECV {address}: {args}")
    if address == "/data/faceTracking/face/rotation/x":
        quaternion[0] = args[0]
    elif address == "/data/faceTracking/face/rotation/y":
        quaternion[1] = args[0]
    elif address == "/data/faceTracking/face/rotation/z":
        quaternion[2] = args[0]
    elif address == "/data/faceTracking/face/rotation/w":
        quaternion[3] = args[0]

    ypr = euler_from_quaternion(*quaternion)
    ypr = [math.degrees(x) for x in ypr]
    print(f"SEND /ypr: {ypr}")
    # it seems only the first value matters
    client.send_message("/ypr", [ypr[1], ypr[0], ypr[2]])

dispatcher = Dispatcher()
# dispatcher.map seems to fail under Python 3.12
dispatcher.set_default_handler(default_handler)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
server = AsyncIOOSCUDPServer((server_ip, server_port), dispatcher, asyncio.get_event_loop())
server.serve()
loop.run_forever()
