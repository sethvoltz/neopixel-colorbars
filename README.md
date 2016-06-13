# Control Script for NeoPixel Color Bars

## Usage

`sudo ./color_bars.py [color_set]`

All colors are specified as HTML hex color. Color set can be empty (all off), 1,
2, 3, or 6 colors as follows:

- One: All bars will be set to the same color
- Two: The two colors will be used to set the outer and inner edges
- Three: Each bar will be set to a specified color
- Six: Each edge will be independently set

## Requirements

Adafruit WS2811/2812 NeoPixel python library must be installed.
