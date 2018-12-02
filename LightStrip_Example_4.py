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

# 10 colors in an array named RAINBOW_COLOR
# Access the colors by RAINBOW_COLOR[number]
# where number is a number from 0 (first color) to
# 9 because there are 10 colors in the array 0-9
RAINBOW_COLOR = (
  (148, 0, 211),
  (75, 0, 130),
  (0, 0, 255),
  (0, 255, 0),
  (255, 255, 0),
  (255, 127, 0),
  (255, 0 , 0),
  (255, 255, 0),
  (255, 0, 255),
  (0, 255, 255) )
    
while True:
    pixels.fill(RAINBOW_COLOR[3])  # This will show green (0, 255, 0)
    """
    # Remove the triple-double quotes above and below to run the for loop
    # len(RAINBOW_COLOR) is the # of colors in the array
    # so this line goes from 0 to 9, changing color_num each time it loops
    # It will go through all 10 colors, then the while True: loop will restart
    # cycling again through colors, 0 through 9, forever and ever.
    for color_num in range(len(RAINBOW_COLOR)):
        pixels.fill(RAINBOW_COLOR[color_num])
        time.sleep(PAUSE_RATE)
    """