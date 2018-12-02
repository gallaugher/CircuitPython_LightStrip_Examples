# CircuitPython LightStrip_Example_RandomColor
from adafruit_circuitplayground.express import cpx
import time
import board  # used to set neopixel pin
import neopixel
import random  # you MUST import random to generate random values

# set up neopixel strip clipped to A1 on the CPX
pixel_pin = board.A1  # the strip is connected to A1
num_pixels = 30  # there are 30 lights in the strip
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=True)

PAUSE_RATE = 0.5 # (one tenth of a second)
    
while True:
    pixels.fill((random.randrange(256), random.randrange(256), random.randrange(256)))
    time.sleep(PAUSE_RATE)
