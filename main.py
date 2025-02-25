# MUST IMPORT LIBRARIES AND MODULES
# argparse parses arguments from the command line, numpy allows us to do math with our matrix/grid, 
# math provides us with other stnadard math functions
import argparse, numpy,  math

# PIL is an image processing library that allows us to open and manipulate our image
from PIL import Image


# MUST DEFINE GRAY SCALE LEVELS TO CONVERT COLOR IN IMAGE
# 0 = black, 255 = white, every other number is a shade of gray
# have to define the character representations for the grayscale - look up example character ramps
# https://paulbourke.net/dataformats/asciiart/, 1 is to about 70 chars and the other is about 10 char
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale2 = " .:-=+*#%@"


# MUST COMPUTE THE AVERAGE BRIGHTNESS FOR EACH TILE
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
# MUST GENERATE AN ASCII CHARACTER FOR EACH TILE DEPENDING ON BRIGHTNESS
def convertToAscii(fileName, columns, scale, moreLevels):
    #given an image and dimensions, return a M * N grid

    #global grayscale variables
    global gscale1, gscale2

    #open image and convert to grayscale
    image = Image.open(fileName).convert('L')

    #store dimensions
    width, height = image.size[0], image.size[1]
    print(f"input image dimensions: {width} by {height}")

    #compute dimensions of individual tiles
    tileWidth = width/columns
    tileHeight = tileWidth/scale
    print(f"tile dimensions: {tileWidth} by {tileHeight}")

    #compute number of rows
    rows = int(height/tileHeight)
    print(f"columns: {columns}, rows: {rows}")

    #verify image is not too small for specified columns
    if columns > width or rows > height:
        print("image too small")
        exit(0)
    
    #define list for all ascii characters
    asciiImg = []

    #generate list of dimensions
    for i in range(rows):
        #y1 = starting y-cord of current row, y2=ending ending y-cord of current row
        y1 = int(i*tileHeight)
        y2 = int((i+1)*tileHeight)

        #ensure last row extends to the full height of the grid
        if i == rows-1:
            y2 = height
        
        #append empty string for each row
        asciiImg.append("")

        #loop for columns
        for j in range(columns):
            #crop image to tile
            x1 = int(j*tileWidth)
            x2 = int ((j+1)*tileWidth)

            #correct the last tile
            if j == columns -1:
                x2 = width
            
            #crop image to extract tile
            img = image.crop((x1, y1, x2, y2))

            #get average luminance - light intensity
            avg = int(averageL(img))

            #look up ascii char and assign to gray scale value
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]
            
            #append ascii char to string
            asciiImg[i] += gsval

    #reutrn string of ascii chars    
    return asciiImg

#main function
# MUST OPEN A NEW TEXT FILE TO OUTPUT TO - DISPLAY FULL IMAGE
def main():
    #create a parser
    descString = "Image to ASCII Art"
    parser = argparse.ArgumentParser(description=descString)

    #add expected arguments, defining a file destination
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--scale', dest='scale', required=False)
    parser.add_argument('--out', dest='outFile', required=False)
    parser.add_argument('--cols', dest='cols', required=False)
    parser.add_argument('--morelevels',dest='moreLevels',action='store_true')

    #parse the arguments
    args = parser.parse_args()
    imgFile = args.imgFile

    #define and set an output file for the image
    outFile = 'out.txt'
    if args.outFile:
        outFile = args.outFile

    #set scale default which suits a courier font
    scale = 0.43
    if args.scale:
        scale = float(args.scale)
    
    #set number of columns
    columns = 80
    if args.cols:
        columns = int(args.cols)
    
    print("generating ASCII art")

    #convert image to ascii text
    asciiImg = convertToAscii(imgFile, columns, scale, args.moreLevels)

    #open file
    f = open(outFile, 'w')

    #write to file
    for row in asciiImg:
        f.write(row + '\n')
    
    #cleanup
    f.close()
    print("ASCII art written %s" % outFile)

#call main
if __name__ == '__main__':
    main()
