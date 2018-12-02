# CircuitPython LightStrip_Example_2 - Color Constants
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
    pixels.fill(RED)
    time.sleep(PAUSE_RATE)
    pixels.fill(ORANGE)
    time.sleep(PAUSE_RATE)
    pixels.fill(YELLOW)
    time.sleep(PAUSE_RATE)
    pixels.fill(GREEN)
    time.sleep(PAUSE_RATE)
    pixels.fill(BLUE)
    time.sleep(PAUSE_RATE)
    pixels.fill(PURPLE)
    time.sleep(PAUSE_RATE)
    pixels.fill(PINK)
    time.sleep(PAUSE_RATE)
