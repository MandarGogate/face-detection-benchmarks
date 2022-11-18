# face-detection-benchmarks
Benchmarking of all publicly accessible implementations of face detection models. A summary is provided in the section below.

System Information:
```
{
    "platform": "Ubuntu 22.04",
    "architecture": "x86_64",
    "processor": "Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz",
    "python_version": "3.9.12 (64 bit)",
}
```

| Model                   |   Img W |   Img H | Min (ms) |   Max (ms) |  Mean (ms) |       FPS |
|:------------------------|--------:|--------:|----------:|-----------:|----------:|----------:|
| Dlib HOG                |    1920 |    1080 | 638.162   |  923.955   | 773.509   |   1.29281 |
| OpenCV Haar             |    1920 |    1080 |  56.5779  |  213.733   |  98.8368  |  10.1177  |
| MTCNN TensorFlow        |    1920 |    1080 | 552.752   | 1203.43    | 686.743   |   1.45615 |
| MTCNN OpenCV            |    1920 |    1080 | 149.676   |  572.335   | 222.918   |   4.48596 |
| InsightFace SCRFD 500MF |    1920 |    1080 |   9.71508 |   14.7526  |  11.7123  |  85.3803  |
| InsightFace SCRFD 10GF  |    1920 |    1080 |  61.5664  |  110.729   |  85.6653  |  11.6733  |
| Ultra-Light-320         |    1920 |    1080 |   4.13775 |   10.1066  |   5.42747 | 184.248   |
| Ultra-Light-640         |    1920 |    1080 |  11.4336  |   18.7521  |  13.8899  |  71.9949  |
| Mediapipe BlazeFace     |    1920 |    1080 |   2.54941 |    4.98104 |   3.06858 | 325.883   |
| Dlib HOG                |    1280 |     720 | 281.621   |  425.411   | 337.644   |   2.9617  |
| OpenCV Haar             |    1280 |     720 |  29.5238  |  102.435   |  49.3472  |  20.2646  |
| MTCNN TensorFlow        |    1280 |     720 | 409.094   |  764.485   | 480.591   |   2.08077 |
| MTCNN OpenCV            |    1280 |     720 |  73.1196  |  331.995   | 109.978   |   9.09273 |
| InsightFace SCRFD 500MF |    1280 |     720 |  10.4578  |   13.1874  |  11.1333  |  89.8208  |
| InsightFace SCRFD 10GF  |    1280 |     720 |  58.6989  |  122.684   |  84.7475  |  11.7998  |
| Ultra-Light-320         |    1280 |     720 |   3.75271 |    6.52814 |   4.387   | 227.946   |
| Ultra-Light-640         |    1280 |     720 |  10.7315  |   17.1158  |  13.6277  |  73.3802  |
| Mediapipe BlazeFace     |    1280 |     720 |   2.25854 |    3.58415 |   2.82665 | 353.775   |
| Dlib HOG                |     640 |     360 |  73.1757  |  103.079   |  88.1228  |  11.3478  |
| OpenCV Haar             |     640 |     360 |  11.5402  |   26.2287  |  16.7382  |  59.7436  |
| MTCNN TensorFlow        |     640 |     360 | 285.993   |  569.742   | 318.214   |   3.14254 |
| MTCNN OpenCV            |     640 |     360 |  22.3444  |   71.3766  |  33.3338  |  29.9996  |
| InsightFace SCRFD 500MF |     640 |     360 |   8.35896 |   13.5674  |   9.99501 | 100.05    |
| InsightFace SCRFD 10GF  |     640 |     360 |  51.2414  |   98.8905  |  75.815   |  13.19    |
| Ultra-Light-320         |     640 |     360 |   3.27849 |    8.59141 |   4.12667 | 242.326   |
| Ultra-Light-640         |     640 |     360 |  10.2892  |   22.0606  |  12.8298  |  77.9437  |
| Mediapipe BlazeFace     |     640 |     360 |   2.17795 |    5.17941 |   2.87227 | 348.156   |
