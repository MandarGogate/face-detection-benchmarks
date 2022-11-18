"""
min
max
mean
FPS
GPU
Model param?
FPS (1080x1920)	FPS (720x1280)	FPS (540x960)
"""
import os

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import statistics
from collections import defaultdict

import pandas as pd

from dlib_hog import benchmark_dlib_hog
from mediapipe_blazeface import benchmark_mediapipe_blazeface
from opecv_haar import benchmark_opencv_haar
from mtcnn_opencv import benchmark_mtcnn_opencv
from mtcnn_facenet_tensorflow import benchmark_mtcnn_tensorflow
from insightface_scrfd import benchmark_insightface_scrfd
from ultra_light import benchmark_ultra_light

stats = defaultdict(list)
for height, width in ((1080, 1920),(720, 1280), (360, 640)):
    for model, func in zip(["Dlib HOG", "OpenCV Haar", "MTCNN TensorFlow", "MTCNN OpenCV", "InsightFace SCRFD 500MF", "InsightFace SCRFD 10GF", "Ultra-Light-320", "Ultra-Light-640", "Mediapipe BlazeFace"],
                           [benchmark_dlib_hog, benchmark_opencv_haar, benchmark_mtcnn_tensorflow, benchmark_mtcnn_opencv, benchmark_insightface_scrfd, benchmark_insightface_scrfd,
                            benchmark_ultra_light, benchmark_ultra_light, benchmark_mediapipe_blazeface]):
        params = dict(width=width, height=height, rep=1, save_out=False)
        if model == "InsightFace SCRFD 10GF":
            params["model"] = "buffalo_l"
        if model == "Ultra-Light-640":
            params["model"] = "640"

        stats["Model"] += [model]
        stats["Img W"] += [width]
        stats["Img H"] += [height]
        time_taken = func(**params)
        stats["Min"] += [min(time_taken) * 1000]
        stats["Max"] += [max(time_taken) * 1000]
        stats["Mean"] += [statistics.mean(time_taken) * 1000]
        stats["FPS"] += [1/statistics.mean(time_taken)]

print(pd.DataFrame(stats).to_markdown(index=False))
