#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2  # 导入模块，opencv的python模块叫cv2
import numpy as np

imgobj = cv2.imread( 'E:\\test3\\test\\data\\234-1.jpg' )  # 读取图像
cv2.namedWindow( "image" )  # 创建窗口并显示的是图像类型
cv2.imshow( "image", imgobj )
cv2.waitKey( 0 )  # 等待事件触发，参数0表示永久等待
cv2.destroyAllWindows()  # 释放窗口

rows, cols, channels = imgobj.shape
# 灰度化
gray_img = cv2.cvtColor( imgobj, cv2.COLOR_BGR2GRAY )

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
num = '234'
filename = 'E:\\test3\\test\\dest\\' + num + '.jpg'
cv2.imwrite( filename, dst )
print( filename )
cv2.namedWindow( "image1" )  # 创建窗口并显示的是图像类型
cv2.imshow( "image1", dst )
cv2.waitKey( 0 )  # 等待事件触发，参数0表示永久等待
cv2.destroyAllWindows()  # 释放窗口