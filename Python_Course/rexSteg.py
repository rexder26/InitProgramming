from stringprep import map_table_b2
from PIL import Image
import os

mapImg = Image.open('testimg.png')
print(mapImg)

# Pending...


# with open('key.txt', 'a+') as map:
#     for y in range(16):
#         for x in range(16):
#             pix = mapImg.getpixel((x, y))
#             print(pix)