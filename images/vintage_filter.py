from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def vintageFilter(image):
    for pixel in image:
        pixel.red = pixel.red * 1.5
        pixel.green = pixel.green * 0.7
        pixel.blue = pixel.blue * 1.5

    return image

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the image before the transform
    image.show()

    # Apply the filter
    # TODO: your code here
    new_image = vintageFilter(image)

    # Show the image after the transform
    new_image.show()
    

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()