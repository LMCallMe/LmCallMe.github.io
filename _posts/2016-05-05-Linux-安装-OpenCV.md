---
title: 安装 OpenCV
layout: post
categories: OpenCV
tag: [OpenCV,Cmake,Linux]
---

# 安装
从[链接](https://github.com/jayrambhia/Install-OpenCV)选择合适的脚本文件

# 在命令行下
``` bash
$ chmod +x opencv.sh
$ ./opencv.sh
```

# 运行OpenCV

## Python

``` python
#!usr/bin/env python
#filename.py
from cv2.cv import *
img = LoadImage("/home/USER/Pictures/python.jpg")
NamedWindow("opencv")
ShowImage("opencv",img)
WaitKey(0)
```
运行：
``` bash
$ python filename.py
```

## C
opencvtest.c
``` C
#include
#include<opencv2/highgui/highgui.hpp>

int main()
{
    IplImage* img = cvLoadImage("/home/USER/Pictures/python.jpg",CV_LOAD_IMAGE_COLOR);
    cvNamedWindow("opencvtest",CV_WINDOW_AUTOSIZE);
    cvShowImage("opencvtest",img);
    cvWaitKey(0);
    cvReleaseImage(&img);
    return 0;
}
```
编译运行：
``` bash
$ gcc -ggdb `pkg-config --cflags opencv` -o `basename opencvtest.c .c` opencvtest.c `pkg-config --libs opencv`
$ ./opencvtest
```

## C++
opencvtest.cpp
``` C++
#include<opencv2/highgui/highgui.hpp>
using namespace cv;

int main()
{

    Mat img = imread("/home/USER/Pictures/python.jpg",CV_LOAD_IMAGE_COLOR);
    imshow("opencvtest",img);
    waitKey(0);

    return 0;
}
```
编译运行
``` bash
$ g++ -ggdb `pkg-config --cflags opencv` -o `basename opencvtest.cpp .cpp` opencvtest.cpp `pkg-config --libs opencv`
$ ./opencvtest
```

# 简化编译使用opencv的程序
bash 脚本 `~/.compile_opencv.sh`

``` bash
#!/bin/bash
echo "compiling $1"
if [[ $1 == *.c ]]
then
    gcc -ggdb `pkg-config --cflags opencv` -o `basename $1 .c` $1 `pkg-config --libs opencv`;
elif [[ $1 == *.cpp ]]
then
    g++ -ggdb `pkg-config --cflags opencv` -o `basename $1 .cpp` $1 `pkg-config --libs opencv`;
else
    echo "Please compile only .c or .cpp files"
fi
echo "Output file => ${1%.*}"
```

添加命令别名：

``` bash
$ alias opencv="~/.compile_opencv.sh"
```

使用该脚本

``` bash
$ opencv opencvtest.c
$ ./opencvtest
```
