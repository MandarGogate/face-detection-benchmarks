# pip install opencv-python
# Download model from https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml

import statistics
import time
from pathlib import Path

import cv2
import imutils


def benchmark_opencv_haar(width=1280, height=720, rep=1, save_out=False):
    detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    time_taken = []
    for _ in range(rep):
        for img_path in Path("./test_data").iterdir():
            image = cv2.imread(str(img_path))
            image = imutils.resize(image, width=width, height=height)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            tic = time.time()
            detections = detector.detectMultiScale(gray, 1.1, 4)
            time_taken.append(time.time() - tic)
            if detections is None:
                continue
            if save_out:
                annotated_image = image.copy()
                for (x, y, w, h) in detections:
                    cv2.rectangle(annotated_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.imwrite('opencv_haar_' + img_path.name, annotated_image)
    return time_taken


if __name__ == '__main__':
    time_taken = benchmark_opencv_haar(save_out=True)
    print(dict(min=min(time_taken) * 1000, max=max(time_taken) * 1000, mean=statistics.mean(time_taken) * 1000))
