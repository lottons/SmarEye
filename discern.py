#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2  # 导入模块，opencv的python模块叫cv2
import matplotlib.pyplot as plt
import numpy as np

# 图像预处理
def img_p(img):
    rows, cols, channels = img.shape
    # 灰度化
    gray_img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )

    # 平滑滤波
    blur = cv2.blur( gray_img, (3, 3) )

    # 二值化
    ret1, th1 = cv2.threshold( blur, 190, 255, cv2.THRESH_BINARY )

    # 透视变换
    b = 50
    pts1 = np.float32( [[b, 0], [cols - b, 0], [0, rows], [cols, rows]] )
    pts2 = np.float32( [[0, 0], [cols, 0], [0, rows], [cols, rows]] )
    M = cv2.getPerspectiveTransform( pts1, pts2 )
    dst = cv2.warpPerspective( th1, M, (cols, rows) )

    return dst