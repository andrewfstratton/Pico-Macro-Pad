# Pico-Macro-Pad
Pico 2W base Pimoroni RGB Key Pad using CircuitPython

# Setup

- Flash adafruit-circuitpython-raspberry_pi_pico2_w-en_GB-10.3.1.UF2 to the Pico (2 W) plugged into the Pimoroni RGB Key Pad

- From adafruit-circuitpython-bundle-10.x-mpy-20260917 add the following into CIRCUITPY in the `lib` folder
  1. adafruit_dotstar.mpy
  2. the whole folder `adafruit_hid`.  **Keep the files in the folder**

- Copy code.py into the drive and test

_Note: May need to run VSCode as admin for reliable connection to serial_

_Trying - Use CircuitPython V2 Extension v0.3.3 - latest version can't find serial port :(_

**N.B. This worked but had to restart VS Code a few times before it did**

Use Shift-Ctrl-P then type Circuit and choose:
- select serial port
- configure board
- open serial monitor (had to restart again)
- I get LOTS of open/close serial port - likely due to CrowdStrike :(

  