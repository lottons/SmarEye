# -*- coding:utf-8 -*-
import cv2

import numpy as np

import time

while True:
    image_path = 'E:\\test3\\test\\data\\target.jpg'
    try:
        f = open( 'E:\\test3\\test\\data\\target.txt', 'r' )
        image_path = f.read()
        print( image_path )
    finally:
        if f:
            f.close()

    Img = cv2.imread( image_path )  # 读入一幅图像
    kernel_2 = np.ones( (2, 2), np.uint8 )  # 2x2的卷积核
    kernel_3 = np.ones( (3, 3), np.uint8 )  # 3x3的卷积核
    kernel_4 = np.ones( (4, 4), np.uint8 )  # 4x4的卷积核
    if Img is not None:  # 判断图片是否读入
        HSV = cv2.cvtColor( Img, cv2.COLOR_BGR2HSV )  # 把BGR图像转换为HSV格式
        '''
        HSV模型中颜色的参数分别是：色调（H），饱和度（S），明度（V）
        下面两个值是要识别的颜色范围
        '''
        Lower = np.array( [35, 43, 46] )  # 要识别颜色的下限
        Upper = np.array( [77, 255, 255] )  # 要识别的颜色的上限
        # mask是把HSV图片中在颜色范围内的区域变成白色，其他区域变成黑色
        mask = cv2.inRange( HSV, Lower, Upper )
        # 下面四行是用卷积进行滤波
        erosion = cv2.erode( mask, kernel_4, iterations=1 )
        erosion = cv2.erode( erosion, kernel_4, iterations=1 )
        dilation = cv2.dilate( erosion, kernel_4, iterations=1 )
        dilation = cv2.dilate( dilation, kernel_4, iterations=1 )
        # target是把原图中的非目标颜色区域去掉剩下的图像
        target = cv2.bitwise_and( Img, Img, mask=dilation )
        # 将滤波后的图像变成二值图像放在binary中
        ret, binary = cv2.threshold( dilation, 127, 255, cv2.THRESH_BINARY )
        # 在binary中发现轮廓，轮廓按照面积从小到大排列
        binary, contours, hierarchy = cv2.findContours( binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )
        p = 0
        result = ["red", "red", "red", "red"]
        for i in contours:  # 遍历所有的轮廓
            x, y, w, h = cv2.boundingRect( i )  # 将轮廓分解为识别对象的左上角坐标和宽、高
            # 在图像上画上矩形（图片、左上角坐标、右下角坐标、颜色、线条宽度）
            cv2.rectangle( Img, (x, y), (x + w, y + h), (255, 0,), 2 )
            # 给识别对象写上标号
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText( Img, str( p ), (x - 10, y + 10), font, 1, (0, 0, 255), 2 )  # 加减10是调整字符位置
            p += 1
            print( '第 ', p, '个的坐标 X: ', x, ' W: ', w, ', Y: ', y, 'H: ', h )
            # 这里判断监测点是否在识别到的颜色块内
            # 第1个监测点坐标 155 180 对应车位1
            if x < 420 and x + w > 420 and y < 170 and y + h > 170:
                result[0] = 'green'

            # 第2个监测点坐标 155 180 对应车位2
            if x < 155 and x + w > 155 and y < 170 and y + h > 170:
                result[1] = 'green'

            # 第3个监测点坐标 155 180 对应车位3
            if x < 400 and x + w > 400 and y < 60 and y + h > 60:
                result[2] = 'green'

            # 第4个监测点坐标 155 180 对应车位4
            if x < 205 and x + w > 205 and y < 60 and y + h > 60:
                result[3] = 'green'

            # if 130 <= x <= 180 and 130 <= y <= 180:
            #     result[3] = "green"
            #
            # if 380 <= x <= 430 and 140 <= y <= 190:
            #     result[0] = "green"
            #
            # if 370 <= x <= 420 and 30 <= y <= 80:
            #     result[2] = "green"
            #
            # if 180 <= x <= 230 and 10 <= y <= 60:
            #     result[1] = "green"

        print( '绿色方块的数量是', p, '个' )  # 终端输出目标数量
        print( result )

        try:
            f = open( 'E:\\test3\\test\\data\\result.txt', 'w' )
            image_path = f.writelines( " ".join( str( i ) for i in result ) )
        finally:
            if f:
                f.close()

        cv2.imshow( 'target', target )
        # cv2.imshow( 'Mask', mask )
        # cv2.imshow( "prod", dilation )
        cv2.imshow( 'Img', Img )
        # cv2.imwrite( 'Img.png', Img )  # 将画上矩形的图形保存到当前目录

    if cv2.waitKey( 5000 ) == ord( 'q' ):
        break
# cap.release()
cv2.destroyAllWindows()
