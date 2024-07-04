# Test the dearVR Spatial Connect Adapter. It should show "connected" status on the menu bar icon.

from pythonosc.udp_client import SimpleUDPClient

upstream_ip = "127.0.0.1"
upstream_port = 7001

client = SimpleUDPClient(upstream_ip, upstream_port)
for i in range(10000000):
    client.send_message("/ypr", [0., 0., 0.])
