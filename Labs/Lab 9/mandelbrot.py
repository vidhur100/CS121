# mandelbrot.py
# Lab 9
#
# Vidhur Busannagari
# November 3rd 2023
# I pledge my honor that I have abided by the Stevens Honor System.


# keep this import line...
from cs5png import PNGImage

# start your Lab 9 functions here:
def mult(c,n):
    """
    Returns the product of c times n but without multiplication. Uses a for loop to make sure that it adds c the correct number of times and then returns the result
    """
    result = 0
    for x in range(n):
        result = result + c
    return result

def update(c,n):
    """
    Starts a new value, z at zero, and then repeatedly updates the value of z using the assignment statement z = z**2 + c for a total of ntimes. Return the final value of z
    """
    z = 0
    for x in range(n):
        z = z ** 2 + c
    return z

def inMSet(c,n):
    """
    Return a Boolean: True if the complex number c is in the Mandelbrot set and False otherwise.
    """
    z = 0
    for x in range(n):
         z = z ** 2 + c
         if abs(z) > 2:
             return False
    return True

def weWantThisPixel( col, row ):
    """ a function that returns True if we want
    the pixel at col, row and False otherwise
    """
    if col % 10 == 0 and row % 10 == 0:
        return True
    else:
        return False

def test():
    """ a function to demonstrate how
    to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()

'''
The image transforms when you replace "and" with "or" in the line of code "if col % 10 == 0 and row % 10 == 0:" resulting picture forms a continuous grid, rather than
a dotted grid every 10 pixels. This change occurs because the 'or' condition evaluates to true if either the column or the row is a multiple of 10.
'''


def scale(pix, pixMax, floatMin, floatMax):
    """ scale takes in
    pix, the CURRENT pixel column (or row)
    pixMax, the total # of pixel columns
    floatMin, the min floating-point value
    floatMax, the max floating-point value
    scale returns the floating-point value that
    corresponds to pix
    """
    return (pix / pixMax) * (floatMax - floatMin) + floatMin

def mset():
    """
    creates a 300x200 image of the Mandelbrot set
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            # here is where you will need
            # to create the complex number, c!
            x = scale(col, width, -2, 1)
            y = scale(row, height, -1, 1)
            c = x + y*1j
            if inMSet(c,25) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()



