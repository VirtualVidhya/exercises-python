# import os
# print("cwd is", os.getcwd())

import warnings
warnings.filterwarnings("ignore", message="iCCP: profile 'ICC Profile'")

from simpleimage import SimpleImage

def darkenImage(filename):
    """
    Makes image passed in darker by halving red, green, blue
    values. Note: changes in image persist after function ends.
    """
    # Demonstrate looping over all the pixels of an image,
    # changing each pixel to be half its original intensity.
    image = SimpleImage(filename)

    for pixel in image:
        pixel.red = pixel.red // 2
        pixel.green = pixel.green // 2
        pixel.blue = pixel.blue // 2

    return image

def redChannelImage(filename):
    """
    Changes the image as follows:
    For every pixel, set green and blue values to 0
    yielding the red channel.
    Return the changed image.
    """
    image = SimpleImage(filename)

    for pixel in image:
        pixel.green = 0
        pixel.blue = 0
        
    return image

def computeLuminosity(red, green, blue):
    """
    Calculates the luminosity of a pixel using NTSC formula
    to weight red, green and blue values appropriately.
    """
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)

def grayscale(filename):
    """
    Reads image from file specified by filename.
    Change the image to be grayscale using the NTSC
    luminosity formula and return it.
    """
    image = SimpleImage(filename)

    for pixel in image:
        luminosity = computeLuminosity(pixel.red, pixel.green, pixel.blue)
        pixel.red = luminosity
        pixel.green = luminosity
        pixel.blue = luminosity

    return image


def main():
    logo_image = SimpleImage("images/nature_wallpaper_1.jpg")

    logo_image = darkenImage("images/nature_wallpaper_1.jpg")
    logo_image.show()

    logo_image = redChannelImage("images/nature_wallpaper_1.jpg")
    logo_image.show()

    logo_image = grayscale("images/nature_wallpaper_1.jpg")
    logo_image.show()

if __name__ == '__main__':
    main()