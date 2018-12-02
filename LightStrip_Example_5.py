# CircuitPython demo - NeoPixel Light Strip Animations
import time
import board
import neopixel
import random
 
from adafruit_circuitplayground.express import cpx
 
pixel_pin = board.A1
num_pixels = 30

# Change these to set speed (lower is faster)
FLASH_RATE = 0.250
SPIN_RATE = 0.100
CHASE_RATE = 0.100

FLASH_COLOR = (0, 0, 255)
SPIN_COLOR = (255, 0, 255)
CYLON_COLOR = (255, 0, 0)

# Define 10 colors here.
# Must be 10 entries.
# Use 0x000000 if you want a blank space.
num_of_rainbow_colors = 10  # since 10 defined below
RAINBOW_COLORS = (
  (148, 0, 211),
  (75, 0, 130),
  (0, 0, 255),
  (0, 255, 0),
  (255, 255, 0),
  (255, 127, 0),
  (255, 0, 0),
  (255, 255, 0),
  (255, 0, 255),
  (0, 255, 255)
)
 
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=True)

def flasher(num_of_times):
    for index in range(num_of_times):
        # Turn on all the pixels to FLASH_COLOR
        pixels.fill(FLASH_COLOR)
        
        # Leave them on for a little bit
        time.sleep(FLASH_RATE)
        
        # Turn off all the NeoPixels
        pixels.fill(0)
        
        # Leave them off for a little bit
        time.sleep(FLASH_RATE)

# strip version
def spinner():
    # Can be any two pixels
    pixel1 = 0
    pixel2 = 5
    
    for index in range(num_pixels):
        # Turn off all the NeoPixels
        pixels.fill(0)
        
        # Turn on two pixels to SPIN_COLOR
        pixels[pixel1] = SPIN_COLOR
        pixels[pixel2] = SPIN_COLOR

        # Increment pixels to move them around the board
        pixel1 = pixel1 + 1
        pixel2 = pixel2 + 1
        
        # Check pixel values
        pixel1 = pixel1 if pixel1 < num_pixels else 0
        pixel2 = pixel2 if pixel2 < num_pixels else 0

def cylon():
    pixel1 = 0
    pixel2 = num_pixels-1
 
    # Scan in one direction
    for step in range(num_pixels/2-1):
        pixels.fill(0)
        
        pixels[pixel1] = CYLON_COLOR
        pixels[pixel2] = CYLON_COLOR
        
        pixel1 = pixel1 + 1
        pixel2 = pixel2 - 1
    
    # Scan back the other direction    
    for step in range(num_pixels/2-1):
        pixels.fill(0)
        
        pixels[pixel1] = CYLON_COLOR
        pixels[pixel2] = CYLON_COLOR
        
        pixel1 = pixel1 - 1
        pixel2 = pixel2 + 1

def bedazzler(num_of_flashes):
    for index in range(num_of_flashes-1):
        # Turn off all the NeoPixels
        pixels.fill(0)
        
        # Turn on a random pixel to a random color
        pixels[random.randrange(num_pixels-1)] = ( random.randrange(256),
                                             random.randrange(256),
                                             random.randrange(256) )

def rainbow(num_of_cycles):
    # Start at the beginning
    start_color = 0
 
    for index in range(num_of_cycles):
        # Turn off all the NeoPixels
        pixels.fill(0)
 
        # Loop through and set pixels
        color = start_color
        for p in range(num_pixels):
            pixels[p] = RAINBOW_COLORS[color]
            color += 1
            color = color if color < len(RAINBOW_COLORS) else 0
            
        # Increment start index into color array
        start_color += 1
        
        # Check value and reset if necessary
        start_color = start_color if start_color < len(RAINBOW_COLORS) else 0

while True:
    flasher(5)  # pass in # of times to flash
    time.sleep(0.25)
    rainbow(5)
    time.sleep(0.25)
    bedazzler(20)  # pass in # of times to flash
    time.sleep(0.25)
    cylon()
    time.sleep(0.25)
    spinner()
    time.sleep(0.25)  
