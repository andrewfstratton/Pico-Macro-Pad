import time
import board
import busio
import usb_hid
from hid_gamepad import Gamepad

from adafruit_bus_device.i2c_device import I2CDevice
import adafruit_dotstar

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

from digitalio import DigitalInOut, Direction, Pull

cs = DigitalInOut(board.GP17)
cs.direction = Direction.OUTPUT
cs.value = 0
num_pixels = 16
pixels = adafruit_dotstar.DotStar(board.GP18, board.GP19, num_pixels, brightness=0.1, auto_write=True)
i2c = busio.I2C(board.GP5, board.GP4)
device = I2CDevice(i2c, 0x20)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
gamepad = Gamepad(usb_hid.devices)

def read_button_bits():
    with device:
        device.write(bytes([0x0]))
        result = bytearray(2)
        device.readinto(result)
        bits = result[0] | result[1] << 8
    return bits

def colourwheel(pos):
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

last_button_bits = 0xFFFF # inverted press state, all buttons released

print("::Started...")
while True:
    button_bits = read_button_bits()

    if last_button_bits != button_bits:
        print(f"button_bits {button_bits:016b}")
        for button in range(16):
            bit_mask = 1 << button
            changed = (last_button_bits & bit_mask) != (button_bits & bit_mask)
            if changed:
                pressed = (button_bits & bit_mask)
                if pressed == 0: # i.e. unset is pressed
                    print(f"+{str(button)} ")
                    gamepad.press_buttons(button + 1)
                else:
                    print(f"-{str(button)} ")
                    gamepad.release_buttons(button + 1)
        last_button_bits = button_bits

        # pixels[2] = colourwheel(2 * 16)  # Map pixel index to 0-255 range

        # kbd.send(Keycode.ENTER)
    time.sleep(0.1) # Debounce
