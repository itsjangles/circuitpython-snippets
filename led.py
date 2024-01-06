import board
import time
import digitalio
# turn on the neopixel to green
import neopixel
import colorsys


print("Hello, CircuitPython!")
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixel.brightness = 0.1

# btn = digitalio.DigitalInOut(direction=digitalio.Direction.INPUT, pull=digitalio.Pull.UP, pin=board.BUTTON_A)
# btn.direction = Direction.INPUT
# btn.pull = Pull.UP
btn = digitalio.DigitalInOut(board.BUTTON)
btn.switch_to_input(pull=digitalio.Pull.UP)
pixel.fill((0, 0, 255))
time.sleep(1)

while True:
    # loop through the colors in HSV
    for i in range(0, 360, 2):
        if not btn.value:
            pixel.brightness = 0
        else:
            pixel.brightness = 0.1
        # convert the HSV color to RGB
        r, g, b = colorsys.hsv_to_rgb(i / 360, 1, 0.5)
        # set the color
        pixel.fill((r, g, b))
        # wait a bit
        time.sleep(0.01)

