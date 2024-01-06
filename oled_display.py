import board
import time
import digitalio
import busio
import displayio
import adafruit_ssd1306


i2c = busio.I2C(board.GP1, board.GP0)
# while not i2c.try_lock():
#     pass
# print("I2C addresses found:", [hex(device_address) for device_address in i2c.scan()])
# i2c.unlock()
try:
    WIDTH = 128
    HEIGHT = 32
    BORDER = 5
    display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3c)
    time.sleep(1)
    display.fill(0)
    display.text('Hello, Jasmine!', 0, 0, 1)
    display.show()

finally:
    print("done")
    # i2c.unlock()
    # i2c.deinit()
# lcd = charlcd.Character_LCD_I2C(i2c, 128, 16, 0x3c)
# lcd = charlcd.Character_LCD_I2C(i2c, 16, 2, 0x3c)
# lcd.message = "Hello, CircuitPython!"
# lcd.backlight = True
# lcd.show_cursor = True
# lcd.display = True
# print(dir(lcd))
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
    time.sleep(0.01)

