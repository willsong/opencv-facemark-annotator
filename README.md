# OpenCV Facemark Trainer

This attempts to fix the bugs in opencv_contrib/modules/face/samples/sample_train_landmark_detector.cpp
Also fixes bugs in modules/face/samples/facemark_demo_lbf.cpp

## Execute python annotator:
```
python annotate.py /Users/willsong/Downloads/archive/CAT_06/ ../assets/test/
```

## Execute:
```
./trainer  -a=/Users/willsong/git/build/annot/ -c=/Users/willsong/git/opencv_contrib/modules/face/samples/sample_config_file.xml -m=/Users/willsong/git/build/runtime/test.yaml -f=/Users/willsong/git/opencv/data/lbpcascades/lbpcascade_frontalface.xml
```

## Execute from lib source:

```
./example_face_sample_train_landmark_detector -a=/Users/willsong/git/build/annot/ -c=/Users/willsong/git/opencv_contrib/modules/face/samples/sample_config_file.xml -m=/Users/willsong/git/build/runtime/test.yaml -f=/Users/willsong/git/opencv/data/lbpcascades/lbpcascade_frontalface.xml
```

## Execute LBF:
```
./trainer  -a=/Users/willsong/git/build/annot/ -c=/Users/willsong/git/opencv_contrib/modules/face/samples/sample_config_file.xml -m=/Users/willsong/git/build/runtime/test.yaml -f=/Users/willsong/git/opencv/data/lbpcascades/lbpcascade_frontalface.xml
```
---
### References
LBF tutorial: https://docs.opencv.org/master/d7/dec/tutorial_facemark_usage.html
Kazemi tutorial: https://docs.opencv.org/master/d6/d49/md__build_master-contrib_docs-lin64_opencv_contrib_modules_face_tutorials_face_landmark_face_landmark_trainer.html
