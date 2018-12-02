# CircuitPython LightStrip_Example_3 - Button Presses
from adafruit_circuitplayground.express import cpx
import time
import board  # used to set neopixel pin
import neopixel

# set up neopixel strip clipped to A1 on the CPX
pixel_pin = board.A1  # the strip is connected to A1
num_pixels = 30  # there are 30 lights in the strip
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=True)

PAUSE_RATE = 0.5 # (one tenth of a second)

# Set some basic colors to use. Feel free to create more.
# Colors are R, G, B
RED = (255, 0, 0)
ORANGE = (255, 40, 0)
YELLOW = (255,165,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (75,0, 200)
PINK = (255, 0, 130)

while True:
    if cpx.button_a and cpx.button_b:
        print("Button A & Button B pressed!")
        pixels.fill((0, 0, 0))
    if cpx.button_a:
        print("Button A pressed!")
        pixels.fill(RED)
    if cpx.button_b:
        print("Button B pressed!")
        pixels.fill(BLUE)
