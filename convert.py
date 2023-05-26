"""
Convert to png
"""

import cv2
import os
from PIL import Image
path = "robo_1/train/images"
for file_name in os.listdir(path):
    im1 = Image.open(path + "/" + file_name)
    im1.save(f"{path}/{file_name[:-4]}.png")
    os.remove(path + "/" + file_name)