# Solution found there:
# http://stackoverflow.com/questions/11960079/padded-fit-with-easy-thumbnails

from PIL import ImageChops


def pad_image(image, **kwargs):
    """Pad an image to make it the same aspect ratio of the desired thumbnail."""

    img_width, img_height = image.size
    des_width, des_height = kwargs['size']
    if not (0.1 < float(des_height) / des_width < 10.0):
        return image  # Doesn't pad the image if the resize ratio is
                      # exaggerated.  Useful in django-filer admin.
    fit = (float(img_width) / des_width,
           float(img_height) / des_height)

    if fit[0] > fit[1]:
        new_image_size = (img_width, int(round(des_height * fit[0])))
        top = (new_image_size[1] - img_height) / 2
        left = 0
    elif fit[0] < fit[1]:
        new_image_size = (int(round(des_width * fit[1])), img_height)
        top = 0
        left = (new_image_size[0] - img_width) / 2
    else:
        return image

    try:
        # Converts the image to add an alpha layer.
        image = image.convert('RGBA')
        # Resizes the image.
        image = image.crop((0, 0, new_image_size[0], new_image_size[1]))
        # Adds an offset to center the image.
        new_image = ImageChops.offset(image, left, top)

        return new_image
    except:
        return image
