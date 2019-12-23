from time import time
from pathlib import Path
from random import seed, choice

from PIL import Image

from app.utils import get_names_from_directory
from app.settings.paths import IMAGES_DIR


EMPTY_PIXEL = (0, 0, 0, 0)
BLACK_PIXEL = (0, 0, 0, 255)
WHITE_PIXEL = (255, 255, 255, 255)

IMAGE_MODE = 'RGBA'
BASE_IMAGE_SIZE = (64, 64)

CONVERTED_SIZE = (640, 640)


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
            print(pixel_tuple)
            merged_pixels.append(BLACK_PIXEL)
            continue
        merged_pixels.append(WHITE_PIXEL)
    return merged_pixels


if __name__ == '__main__':
    merged_pixels = merge_pixels(get_all_parts('danilok'))
    merged_image = Image.new(IMAGE_MODE, BASE_IMAGE_SIZE)
    merged_image.putdata(merged_pixels)
    resized_image = merged_image.resize(CONVERTED_SIZE)
    resized_image.show()

