# -*- coding: utf-8 -*-
# Standard Library
import io

# Plone
from PIL import Image


def get_image(image):
    original_file = io.BytesIO()
    original_file.write(image.data)
    original_file.seek(0)
    value = Image.open(original_file)
    return value


def get_dominant_color(image):
    image = get_image(image)
    w, h = image.size
    pixels = image.getcolors(w * h)

    most_used_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_used_pixel[0]:
            most_used_pixel = (count, colour)
    most_used_pixel = most_used_pixel[1]
    value = 'rgb({})'.format(','.join(str(i) for i in most_used_pixel))
    return value


def get_ratio(image):
    image = get_image(image)
    w, h = image.size
    if w == -1 and h == -1:
        return None
    value = '{}'.format((float(h) / float(w)) * 100)
    return value
