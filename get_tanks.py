"""
Collect only those images that contain tanks
"""

import os

path_to_files = "robo_1/train/labels/"
path_to_imgs = "robo_1/train/images/"


for filename in os.listdir(path_to_files):
    with open(path_to_files+filename, "r", encoding="utf-8") as f:
        keep = []

        for line in f:
            
            # class number in dataset
            if int(line.split(" ")[0]) == 2:
                line = "0" + line[1:]
                keep.append(line.strip() + "\n")

    
    if keep:
        with open(path_to_files+filename, "w", encoding="utf-8") as f:
            f.writelines(keep)
    else:
        os.remove(path_to_files + filename)
        os.remove(path_to_imgs + filename[:-4] + ".jpg")
