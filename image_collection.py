#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2
import numpy as np

cap = cv2.VideoCapture( 1 )

cap.set( 3, 320 )
cap.set( 4, 240 )

ret, frame = cap.read()
rows, cols, channels = frame.shape
print( cols, rows, channels )


def get_point(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print( x, y )


cv2.namedWindow( "image" )
cv2.setMouseCallback( "image", get_point )


# 图像预处理
def img_p(img):
    # 灰度化
    gray_img = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )

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


num = input( "num:" )
print( num )
while True:
    # 读取图像
    ret, frame = cap.read()

    dst = img_p( frame )

    k = cv2.waitKey( 10 )
    if k == ord( 'q' ):
        break
    elif k == ord( 's' ):
        filename = r'./num_data/' + num + '.jpg'
        cv2.imwrite( filename, dst )
        print( filename )
        num = input( "num:" )
        print( num )

    cv2.imshow( "image", dst )

cap.release()
cv2.destroyAllWindows()