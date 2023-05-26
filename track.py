"""
Load best weights and track tank on video
"""

from ultralytics import YOLO


# /home/daria/ucu/year_3/ml/project/drone-footage-annotations/video_153/data
# /home/daria/ucu/year_3/ml/project/drone-footage-annotations/video_76/data
# /home/daria/ucu/year_3/ml/project/drone-footage-annotations/video_114/data
# /home/daria/ucu/year_3/ml/project/drone-footage-annotations/video_138/data

model = YOLO("GAMES/runs/detect/train/weights/best.pt")

results = model.track(source="/home/daria/ucu/year_3/ml/project/drone-footage-annotations/video_4/data", show=True, save=True) 
