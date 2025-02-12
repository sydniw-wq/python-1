# MUST IMPORT LIBRARIES AND MODULES
# argparse parses arguments from the command line, numpy allows us to do math with our matrix/grid, 
# math provides us with other stnadard math functions
import argparse, numpy,  math

# PIL is an image processing library that allows us to open and manipulate our image
from PIL import IMAGE


# MUST DEFINE GRAY SCALE LEVELS TO CONVERT COLOR IN IMAGE
# 0 = black, 255 = white, every other number is a shade of gray
# have to define the character representations for the grayscale - look up example character ramps
# https://paulbourke.net/dataformats/asciiart/, 1 is to about 70 chars and the other is about 10 char
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale2 = " .:-=+*#%@"

# now will define average function which takes in image (already in grayscale)
# and coomputes the average pixel value of the grayscale intensities
def averageL(image):
    #given PIL grayscale image, onvert to numpy array
    image1 = numpy.array(image)

    #get shape dimensions
    width, height = image1.shape

    #compute average pixel value
    return numpy.average(image1.reshape(width * height))


# MUST SPLIT UP IMAGE INTO AN M * N GRID 

# MUST COMPUTE THE AVERAGE BRIGHTNESS FOR EACH TILE

# MUST GENERATE AN ASCII CHARACTER FOR EACH TILE DEPENDING ON BRIGHTNESS

# MUST OPEN A NEW TEXT FILE TO OUTPUT TO - DISPLAY FULL IMAGE