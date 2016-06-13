#!/usr/bin/python

import sys
from neopixel import *
from itertools import chain, repeat

# LED strip configuration:
LED_COUNT      = 6       # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# Define functions which animate LEDs in various ways.
def setColors(strip, colors):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, colors[i])
		strip.show()

def hexToRgb(value):
	value = value.lstrip('#')
	lv = len(value)
	colors = list(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
	# Fix for GRB colors
	return Color(colors[1], colors[0], colors[2])

def main(colors):
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

	# Intialize the library (must be called once before other functions).
	strip.begin()

	numColors = len(colors)
	colorSet = []

	if numColors >= 6:
		colorSet = map(hexToRgb, colors[0:6])
	elif numColors >= 3:
		# colorSet = list(chain.from_iterable(repeat(x, 3) for x in colors[0:3]))
		colorSet = map(hexToRgb, (colors[0:1] * 2) + (colors[1:2] * 2) + (colors[2:3] * 2))
	elif numColors == 2:
		colorSet = map(hexToRgb, (colors[0:2] * 3))
	elif numColors == 1:
		colorSet = map(hexToRgb, (colors[0:1] * 6))
	else:
		colorSet = [0] * 6

	setColors(strip, colorSet)

if __name__ == '__main__':
	main(sys.argv[1:])
