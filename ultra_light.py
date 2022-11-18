# https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB
# pip install face-detectors



import statistics
import time
from pathlib import Path

import cv2
import imutils
from face_detectors import *
from face_detectors.utils import annotate_image


def benchmark_ultra_light(width=640, height=480, rep=1, save_out=True, model="320"):
    if model == "640":
        detector = Ultralight640Detector()
    else:
        detector = Ultralight320Detector()
    time_taken = []
    for _ in range(rep):
        for img_path in Path("./test_data").iterdir():
            image = cv2.imread(str(img_path))
            image = imutils.resize(image, width=width, height=height)
            tic = time.time()
            faces = detector.detect_faces(image)
            time_taken.append(time.time() - tic)

            if save_out:
                annotated_image = image.copy()
                annotated_image = annotate_image(annotated_image, faces, width=3)
                cv2.imwrite('retina_face_' + img_path.name, annotated_image)
    return time_taken


if __name__ == '__main__':
    time_taken = benchmark_ultra_light()
    print(dict(min=min(time_taken) * 1000, max=max(time_taken) * 1000, mean=statistics.mean(time_taken) * 1000))
