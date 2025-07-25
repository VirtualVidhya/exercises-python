import warnings
warnings.filterwarnings("ignore", message="iCCP: profile 'ICC Profile'")

from simpleimage import SimpleImage

"""
This program shows an example of "greenscreening" (actually
"redscreening" in this case).  This is where we replace the
pixels of a certain color intensity in a particular channel
(here, we use red) with the pixels from another image.
"""


INTENSITY_THRESHOLD = 1.6


def redScreen(main_filename, back_filename):
    """
    Implements the notion of "redscreening".  That is,
    the image in the main_filename has its "sufficiently"
    red pixels replaced with pized from the corresponding x,y
    location in the image in the file back_filename.
    Returns the resulting "redscreened" image.
    """
    image = SimpleImage(main_filename)
    back = SimpleImage(back_filename)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        # See if this pixel is "sufficiently" red
        if pixel.red >= average * INTENSITY_THRESHOLD:
            # If so, we get the corresponding pixel from the
            # back image and overwrite the pixel in
            # the main image with that from the back image.
            x = pixel.x
            y = pixel.y
            image.set_pixel(x, y, back.get_pixel(x, y))

    return image

def greenScreen(main_filename, back_filename):
    """
    Implements the notion of "greenscreening".  That is,
    the image in the main_filename has its "sufficiently"
    green pixels replaced with pized from the corresponding x,y
    location in the image in the file back_filename.
    Returns the resulting "greenscreened" image.
    """
    image = SimpleImage(main_filename)
    back = SimpleImage(back_filename)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        # See if this pixel is "sufficiently" green
        if pixel.green >= average * INTENSITY_THRESHOLD:
            # If so, we get the corresponding pixel from the
            # back image and overwrite the pixel in
            # the main image with that from the back image.
            x = pixel.x
            y = pixel.y
            image.set_pixel(x, y, back.get_pixel(x, y))

    return image

def blueScreen(main_filename, back_filename):
    """
    Implements the notion of "bluescreening".  That is,
    the image in the main_filename has its "sufficiently"
    blue pixels replaced with pized from the corresponding x,y
    location in the image in the file back_filename.
    Returns the resulting "bluescreened" image.
    """
    image = SimpleImage(main_filename)
    back = SimpleImage(back_filename)
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        # See if this pixel is "sufficiently" blue
        if pixel.blue >= average * INTENSITY_THRESHOLD:
            # If so, we get the corresponding pixel from the
            # back image and overwrite the pixel in
            # the main image with that from the back image.
            x = pixel.x
            y = pixel.y
            image.set_pixel(x, y, back.get_pixel(x, y))

    return image


def main():
    """
    Run your desired image manipulation functions here.
    You should store the return value (image) and then
    call .show() to visualize the output of your program.
    """
    main_og_img = SimpleImage('images/nature_wallpaper_1.jpg')
    main_og_img.show()

    greenscreened_img = greenScreen('images/green_screen.jpg', 'images/nature_wallpaper_1.jpg')
    greenscreened_img.show()

    # back_og_img = SimpleImage('images/nature_wallpaper_2.jpg')
    # back_og_img.show()

    # redscreened_img = redScreen('images/nature_wallpaper_1.jpg', 'images/nature_wallpaper_2.jpg')
    # redscreened_img.show()

    # greenscreened_img = greenScreen('images/nature_wallpaper_1.jpg', 'images/nature_wallpaper_2.jpg')
    # greenscreened_img.show()

    # bluescreened_img = blueScreen('images/nature_wallpaper_1.jpg', 'images/nature_wallpaper_2.jpg')
    # bluescreened_img.show()


if __name__ == '__main__':
    main()