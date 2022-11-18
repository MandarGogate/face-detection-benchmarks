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
|:------------------------|--------:|--------:|---------:|-----------:|-----------:|----------:|
| Dlib HOG                |    1920 |    1080 |  636.942 |    886.825 |    779.103 |   1.28353 |
| OpenCV Haar             |    1920 |    1080 |   55.516 |    197.945 |    99.9447 |  10.0055  |
| MTCNN TensorFlow        |    1920 |    1080 |  540.366 |     1033.1 |    674.493 |   1.48259 |
| MTCNN OpenCV            |    1920 |    1080 |  173.266 |    488.847 |    218.475 |   4.57719 |
| InsightFace SCRFD 500MF |    1920 |    1080 |  10.4434 |    10.9782 |    10.7576 |  92.9576  |
| InsightFace SCRFD 10GF  |    1920 |    1080 |  52.9945 |    80.3773 |    66.6845 |  14.996   |
| Ultra-Light-320         |    1920 |    1080 |  11.8544 |    13.2885 |    12.2064 |  81.9242  |
| Ultra-Light-640         |    1920 |    1080 |  12.7499 |    18.2073 |    14.9963 |  66.6831  |
| Mediapipe BlazeFace     |    1920 |    1080 |  2.65121 |    6.02198 |    3.45308 | 289.596   |
| Dlib HOG                |    1280 |     720 |  301.298 |    392.808 |    340.901 |   2.9334  |
| OpenCV Haar             |    1280 |     720 |  30.9384 |    99.5162 |    51.7451 |  19.3255  |
| MTCNN TensorFlow        |    1280 |     720 |  421.498 |     1023.8 |    535.901 |   1.86602 |
| MTCNN OpenCV            |    1280 |     720 |  79.9129 |    280.109 |    116.468 |   8.58604 |
| InsightFace SCRFD 500MF |    1280 |     720 |  10.5078 |    13.2008 |    11.5485 |  86.5917  |
| InsightFace SCRFD 10GF  |    1280 |     720 |   76.921 |     80.689 |     78.192 |  12.789   |
| Ultra-Light-320         |    1280 |     720 |  11.4899 |    17.1208 |    13.6027 |  73.5146  |
| Ultra-Light-640         |    1280 |     720 |  12.0466 |    21.8108 |    14.1258 |  70.7924  |
| Mediapipe BlazeFace     |    1280 |     720 |  2.75111 |    3.63278 |    3.01914 | 331.22    |
| Dlib HOG                |     640 |     360 |  71.8672 |      100.7 |    86.6145 |  11.5454  |
| OpenCV Haar             |     640 |     360 |  14.3704 |    25.1811 |     17.261 |  57.9342  |
| MTCNN TensorFlow        |     640 |     360 |  299.818 |    517.378 |    348.893 |   2.86621 |
| MTCNN OpenCV            |     640 |     360 |  26.7386 |    68.7175 |    34.8941 |  28.6581  |
| InsightFace SCRFD 500MF |     640 |     360 |  10.0932 |    11.7304 |    10.7046 |  93.4174  |
| InsightFace SCRFD 10GF  |     640 |     360 |  53.1487 |    81.3539 |    63.5975 |  15.7239  |
| Ultra-Light-320         |     640 |     360 |  10.7741 |    15.9087 |    12.4311 |  80.4433  |
| Ultra-Light-640         |     640 |     360 |  11.4462 |    15.1107 |    12.5067 |  79.9574  |
| Mediapipe BlazeFace     |     640 |     360 |   2.6679 |     3.9227 |    3.11286 | 321.248   |
