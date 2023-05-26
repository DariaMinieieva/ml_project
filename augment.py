"""
Reduce quality of game dataset
"""

import os
import cv2
import imutils


path = "game_dataset/test/game/images"
path_to_save = "game_dataset/aug_test"

for filename in os.listdir(path):
    image = cv2.imread(path + "/" + filename)

    before = image.shape[1]


    resized = imutils.resize(image, width=int(0.3*before))
    revert = imutils.resize(resized, width=before)

    cv2.imwrite(path_to_save + "/" + filename, revert)
