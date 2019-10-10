#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 对样本进行预处理
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dropout, Flatten, Dense
from keras.callbacks import ModelCheckpoint

# 设置训练参数
nb_train_samples = 10000  # 训练样本数
nb_validation_samples = 1000  # 测试样本数
nb_epoch = 20  # 训练轮数
batch_size = 32  # 批次大小

# 图片尺寸
img_width, img_height, channels = 233, 240, 1
input_shape = (img_width, img_height, channels)

# 训练和测试数据路径
target = 'D:\\Temp\\smart_eye\\num_data\\'
train_data_dir = target + 'train\\'
validation_data_dir = target + 'validation\\'

# 图片生成器ImageDataGenerator
train_pic_gen = ImageDataGenerator(
    rescale=1. / 255,  # 对输入图片进行归一化到0-1区间
    # 根据需求进行进一步调整
    # rotation_range=5,
    # width_shift_range=0.1,
    # height_shift_range=0.1,
)

# 测试集不做变形处理，只需归一化。
validation_pic_gen = ImageDataGenerator( rescale=1. / 255 )

# 按文件夹生成训练集流和标签
train_flow = train_pic_gen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),  # 调整图像大小
    batch_size=batch_size,
    color_mode='grayscale',  # 输入图片为灰度图片
    # color_mode='rgb',
    classes=[str( i ) for i in range( 1, 65, 1 )],
    class_mode='categorical' )

# 按文件夹生成测试集流和标签，
validation_flow = validation_pic_gen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),  # 调整图像大小
    batch_size=batch_size,
    color_mode='grayscale',  # 输入图片为灰度图片
    # color_mode='rgb',
    classes=[str( i ) for i in range( 1, 65, 1 )],  # 标签
    class_mode='categorical'  # 多分类
)

# 搭建模型
model = Sequential()

model.add( Conv2D( 32, (3, 3), activation='relu', input_shape=input_shape ) )
model.add( Conv2D( 32, (3, 3), activation='relu' ) )
model.add( MaxPooling2D( pool_size=(2, 2) ) )
model.add( Dropout( 0.25 ) )

model.add( Conv2D( 64, (3, 3), activation='relu' ) )
model.add( Conv2D( 64, (3, 3), activation='relu' ) )
model.add( MaxPooling2D( pool_size=(2, 2) ) )
model.add( Dropout( 0.25 ) )

model.add( Flatten() )
model.add( Dense( 256, activation='relu' ) )
model.add( Dropout( 0.5 ) )
model.add( Dense( 64, activation='softmax' ) )

model.compile( loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'] )

model.summary()

# 回调函数，保存最佳训练参数
checkpointer = ModelCheckpoint( filepath="D:\\Temp\\smart_eye\\num_data\\weights\\weights.h5", verbose=1,
                                save_best_only=True )

# 导入上次训练的权重
try:
    model.load_weights( 'D:\\Temp\\smart_eye\\num_data\\weights\\weights.h5' )
    print( "load weights..." )
except:
    print( "not weights" )
    pass

# 数据流训练API
model.fit_generator(
    train_flow,
    steps_per_epoch=nb_train_samples / batch_size,
    epochs=nb_epoch,
    validation_data=validation_flow,
    validation_steps=nb_validation_samples / batch_size,
    callbacks=[checkpointer]
)
