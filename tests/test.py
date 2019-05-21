#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# Xiang Wang @ 2019-05-20 17:51:50


from pillow_snippet import convert
from pillow_snippet.mask import Mask

from PIL import Image


origin_image = Image.open('example.jpg')

image = origin_image.resize((200, 200))
circle_image = convert.circle_image(image)
circle_image.save("test_result/circle_image.png")

mask = Mask(origin_image)
exclude_white_image = mask.get_exclude_white_image(tolerance=80)
exclude_white_image.save("test_result/exclude_white_image.png")
