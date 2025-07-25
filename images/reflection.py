"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def make_reflected(filename):
    original = SimpleImage(filename)
    width = original.width
    height = original.height

    # Create blank output image
    output = SimpleImage.blank(width, height * 2)

    # Copy original into top half
    for y in range(height):
        for x in range(width):
            src = original.get_pixel(x, y)
            dst = output.get_pixel(x, y)
            dst.red, dst.green, dst.blue = src.red, src.green, src.blue

    # Create mirrored bottom half
    for y in range(height):
        for x in range(width):
            src = original.get_pixel(x, y)
            reflected_y = (2 * height - 1) - y
            dst = output.get_pixel(x, reflected_y)
            dst.red, dst.green, dst.blue = src.red, src.green, src.blue

    return output

def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    original = SimpleImage('images/mt_rainier.jpg')
    original.show()
    reflected = make_reflected('images/mt_rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
