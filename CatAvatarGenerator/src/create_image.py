from random import seed, choice
from io import BytesIO
from base64 import b64encode


from PIL import Image

from CatAvatarGenerator.utils import get_names_from_directory
from CatAvatarGenerator.settings.paths import IMAGES_DIR
from CatAvatarGenerator.settings.config import (
    WHITE_PIXEL, BLACK_PIXEL, BASE_IMAGE_SIZE, IMAGE_MODE, CONVERTED_SIZE
)


def make_pixels(image_path):
    image = Image.open(image_path)
    return list(image.getdata())


def get_all_parts(user_name, image_directory=IMAGES_DIR):
    seed(user_name)
    parts_pixels = []
    parts_directories = get_names_from_directory(image_directory)
    for part_dir in parts_directories:
        image_name = choice(get_names_from_directory(part_dir))
        parts_pixels.append(make_pixels(image_name))
    return parts_pixels


def merge_pixels(pixels):
    merged_pixels = []
    for i, pixel_tuple in enumerate(zip(*pixels)):
        if BLACK_PIXEL in pixel_tuple:
            merged_pixels.append(BLACK_PIXEL)
            continue
        merged_pixels.append(WHITE_PIXEL)
    return merged_pixels


def create_cat_avatar(user_id):
    merged_pixels = merge_pixels(get_all_parts(user_id))

    merged_image = Image.new(IMAGE_MODE, BASE_IMAGE_SIZE)
    merged_image.putdata(merged_pixels)
    resized_image = merged_image.resize(CONVERTED_SIZE, Image.NEAREST)

    with BytesIO() as stream:
        resized_image.save(stream, 'PNG', quality=100)
        stream.seek(0)
        image_stream = b64encode(stream.getvalue())
    return image_stream
