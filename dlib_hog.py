# http://dlib.net/face_detector.py.html
# pip install dlib

import statistics
import time
from pathlib import Path

import cv2
import imutils

import dlib


def benchmark_dlib_hog(width=1280, height=720, rep=10, save_out=False):
    detector = dlib.get_frontal_face_detector()
    time_taken = []
    for _ in range(rep):
        for img_path in Path("./test_data").iterdir():
            image = cv2.imread(str(img_path))
            image = imutils.resize(image, width=width, height=height)
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            tic = time.time()
            detections = detector(rgb_image, 1)
            time_taken.append(time.time() - tic)
            if detections is None:
                continue
            if save_out:
                annotated_image = image.copy()
                for detection in detections:
                    cv2.rectangle(annotated_image, (detection.left(), detection.top()),
                                  (detection.right(), detection.bottom()), (255, 0, 0), 2)
                cv2.imwrite('dlib_hog_' + img_path.name, annotated_image)
    return time_taken


if __name__ == '__main__':
    time_taken = benchmark_dlib_hog(save_out=False)
    print(dict(min=min(time_taken) * 1000, max=max(time_taken) * 1000, mean=statistics.mean(time_taken) * 1000))
