# https://google.github.io/mediapipe/solutions/face_detection.html
# pip install mediapipe
import statistics
import time
from pathlib import Path

import cv2
import imutils

import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


def benchmark_mediapipe_blazeface(width=1280, height=720, model_selection=0, rep=10, save_out=False):
    time_taken = []
    with mp_face_detection.FaceDetection(
            model_selection=model_selection, min_detection_confidence=0.5) as face_detection:
        for _ in range(rep):
            for img_path in Path("./test_data").iterdir():
                image = cv2.imread(str(img_path))
                image = imutils.resize(image, width=width, height=height)
                rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                tic = time.time()
                results = face_detection.process(rgb_image)
                time_taken.append(time.time() - tic)
                if not results.detections:
                    continue
                if save_out:
                    annotated_image = image.copy()
                    for detection in results.detections:
                        mp_drawing.draw_detection(annotated_image, detection)
                    cv2.imwrite('mediapipe_blazeface_' + img_path.name, annotated_image)
    return time_taken


if __name__ == '__main__':
    time_taken = benchmark_mediapipe_blazeface()
    print(dict(min=min(time_taken) * 1000, max=max(time_taken) * 1000, mean=statistics.mean(time_taken) * 1000))
