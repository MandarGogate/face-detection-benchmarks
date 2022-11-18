# https://github.com/deepinsight/insightface/tree/master/python-package
# pip install insightface
# insightface-cli model.download buffalo_l
# insightface-cli model.download buffalo_sc
import statistics
import time
from pathlib import Path

import cv2
import imutils
from insightface.app import FaceAnalysis


def benchmark_insightface_scrfd(width=640, height=480, rep=1, save_out=False, model="buffalo_sc"):
    app = FaceAnalysis(name=model, allowed_modules=['detection'],
                       providers=['CPUExecutionProvider'])  # enable detection model only
    app.prepare(ctx_id=0, det_size=(640, 640))
    # detector.prepare(ctx_id=0, input_size=(width, height))
    time_taken = []
    for _ in range(rep):
        for img_path in Path("./test_data").iterdir():
            image = cv2.imread(str(img_path))
            image = imutils.resize(image, width=width, height=height)
            tic = time.time()
            faces = app.get(image)
            time_taken.append(time.time() - tic)
            if save_out:
                rimg = app.draw_on(image, faces)
                cv2.imwrite('mediapipe_blazeface_' + img_path.name, rimg)
    return time_taken


if __name__ == '__main__':
    time_taken = benchmark_insightface_scrfd()
    print(dict(min=min(time_taken) * 1000, max=max(time_taken) * 1000, mean=statistics.mean(time_taken) * 1000))
