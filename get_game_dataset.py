"""
Divide dataset that contains game data
on real world data and game data
"""

import os
from PIL import Image
import shutil

path = "game_dataset/train"

path_to_save_game = "game_dataset/game"
path_to_save_life = "game_dataset/life"

for filename in os.listdir(path + "/images"):
    im1 = Image.open(path + "/images/" + filename)

    if filename[:4] == "shot":
        im1.save(f"{path_to_save_game}/images/{filename[:-4]}.png")
        shutil.copyfile(path + "/labels/"+ filename[:-4] + ".txt" , path_to_save_game + "/labels/"+ filename[:-4] + ".txt")
    else:
        im1.save(f"{path_to_save_life}/images/{filename[:-4]}.png")
        shutil.copyfile(path + "/labels/"+ filename[:-4] + ".txt" , path_to_save_life + "/labels/"+ filename[:-4] + ".txt")

