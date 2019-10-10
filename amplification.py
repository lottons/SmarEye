#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
生成多个样本
author:Administrator
datetime:2018/3/24/024 18:46
software: PyCharm
"""

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os


# 生成文件夹
def ensure_dir(dir_path):
    if not os.path.exists( dir_path ):
        try:
            os.makedirs( dir_path )
        except OSError:
            pass


# 图片生成器ImageDataGenerator
pic_gen = ImageDataGenerator(
    rotation_range=5,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.2,
    zoom_range=0.2,
    fill_mode='nearest' )


# 生成图片
def img_create(img_dir, save_dir, img_prefix, num=100):
    img = load_img(img_dir)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)
    img_flow = pic_gen.flow(
        x,
        batch_size=1,
        save_to_dir=save_dir,
        save_prefix=img_prefix,
        save_format="jpg"
    )
    i = 0
    for batch in img_flow:
        i += 1
        if i > num:
            break


# 生成训练集
list1 = ['1234','234']
for img_prefix in list1:
    # img_prefix = str( i )
    img_dir = 'E:\\test3\\test\\dest\\' + img_prefix + '.jpg'
    save_dir = 'E:\\test3\\test\\num_data\\train\\' + img_prefix
    ensure_dir( save_dir )
    img_create( img_dir, save_dir, img_prefix, num=200 )
    print( "train: ", img_prefix )

# 生成测试集
for img_prefix in list1:
    # img_prefix = str( i )
    img_dir = 'E:\\test3\\test\\dest\\' + img_prefix + '.jpg'
    save_dir = 'E:\\test3\\test\\num_data\\validation\\' + img_prefix
    ensure_dir( save_dir )
    img_create( img_dir, save_dir, img_prefix, num=100 )
    print( "validation: ", img_prefix )