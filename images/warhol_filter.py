"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba_dog.jpg'


def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    
    for px in patch:
        # Scale each channel
        new_red   = px.red   * red_scale
        new_green = px.green * green_scale
        new_blue  = px.blue  * blue_scale
        # Cap values to 255
        px.red   = min(int(new_red),   255)
        px.green = min(int(new_green), 255)
        px.blue  = min(int(new_blue),  255)

    return patch

def add_patch(final_image, patch, row, col):
    """
    Draw the `patch` onto `final_image` at grid position (row, col).
    """
    x_offset = col * PATCH_SIZE
    y_offset = row * PATCH_SIZE
    for y in range(PATCH_SIZE):
        for x in range(PATCH_SIZE):
            src_px = patch.get_pixel(x, y)
            dst_px = final_image.get_pixel(x + x_offset, y + y_offset)
            dst_px.red, dst_px.green, dst_px.blue = src_px.red, src_px.green, src_px.blue

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    
    scales = [
        (1.5, 0.0, 1.5),  # pink
        (0.0, 1.5, 1.0),  # green‑yellow
        (1.0, 1.0, 1.0),  # cyan
        (1.5, 1.5, 0.0),  # orange
        (1.2, 1.0, 0.8),  # teal
        (0.0, 0.5, 1.5)   # purple
    ]

    idx = 0
    for row in range(N_ROWS):
        for col in range(N_COLS):
            red_scale, green_scale, blue_scale = scales[idx]
            patch = make_recolored_patch(red_scale, green_scale, blue_scale)
            add_patch(final_image, patch, row, col)
            idx += 1

    final_image.show()

if __name__ == '__main__':
    main()