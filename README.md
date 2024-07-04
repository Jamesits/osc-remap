# osc-remap

Open Sound Control data remap script, for converting iOS [Data OSC](https://apps.apple.com/us/app/data-osc/id6447833736) app face tracking data to dearVR Spatial Connect Adapter.

## Setup

0. Install dearVR PRO 2 or dearVR Monitor according to your needs. During installation, select the option to install the Spatial Connect Adapter.
0. Start the dearVR Spatial Connect Adapter *first*, then open your DAW and load the dearVR VST plugin.
0. In the Spatial Connect Adapter configuration window, select Network -> Protocol -> OSC Headtracker, and Port 7001.
0. Launch `python server.py` on the same machine.
0. Launch the Data OSC app on your iOS device, and configure the OSC settings to point to the IP address of the machine running the server, and port 7002.
0. In the Data OSC app, enable Face Tracking with the default args.
0. Profit

## Known Issues

- Data OSC (as of 1.1.0) doesn't keep the screen on, and stops sending data after screen lock; disable automatic screen lock in iOS settings for prolonged use.
- dearVR Spatial Connect Adapter on macOS does not work well with any application that tampers the menu bar icons (e.g. Bartender or Ice); close them before using the adapter.
- dearVR VST plugins perform very badly when loaded by any ROGUE AMOEBA applications (Audio Hijack, Loopback, SoundSource, etc.); it's better to use them in DAWs.
- dearVR VST plugins currently only support head tracking in the horizontal plane (rotation).
