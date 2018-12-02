# CircuitPython LightStrip_Example_1
from adafruit_circuitplayground.express import cpx
import time
import board  # used to set neopixel pin
import neopixel

# set up neopixel strip clipped to A1 on the CPX
pixel_pin = board.A1  # the strip is connected to A1
num_pixels = 30  # there are 30 lights in the strip
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=True)

PAUSE_RATE = 0.5 # (one tenth of a second)
    
while True:
    pixels.fill((255, 0, 0))
    time.sleep(PAUSE_RATE)
    pixels.fill((0, 255, 0))
    time.sleep(PAUSE_RATE)
    pixels.fill((0, 0, 255))
    time.sleep(PAUSE_RATE)

