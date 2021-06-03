# -*- coding: utf-8 -*-
"""Cnn cat or dog .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EZXe-cXQUTS4Jofq8r3q9jM1vFkRqD-L
"""

from zipfile import ZipFile
filename="/content/drive/MyDrive/dataset.zip"
with ZipFile(filename,'r') as zip:
  zip.extractall()
  print("finsih")

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten

# Initialising the CNN
model=Sequential()
# Step 1 - Convolution
model.add(Conv2D(filters=32,kernel_size=(3,3),input_shape=(64,64,3),activation="relu"))
# step 2 -Pooling
model.add(MaxPooling2D(pool_size=(2,2)))
# step 1 -convolution
model.add(Conv2D(filters=32,kernel_size=(3,3),activation="relu"))
# step 2 - Pooling
model.add(MaxPooling2D(pool_size=(2,2)))
# step 3 - Flattening
model.add(Flatten())
# step 4 - full connection
model.add(Dense(units=128,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))
# compiling the cnn
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
train_set = train_datagen.flow_from_directory(
        '/content/dataset/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
test_set = test_datagen.flow_from_directory(
        '/content/dataset/test_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
model.fit(
        train_set,
        steps_per_epoch=int(7000/32),
        epochs=5,
        validation_data=test_set,
        validation_steps=2000/32)

from keras.preprocessing import image
import numpy as np

test_image=image.load_img('/content/dataset/single_prediction/cat_or_dog_1.jpg',target_size=(64,64))
test_image=image.img_to_array(test_image)
test_image=np.expand_dims(test_image,axis=0)
result=model.predict(test_image)
train_set.class_indices
if result[0][0]==1:
  print("dog")
else:
  print("cat")

