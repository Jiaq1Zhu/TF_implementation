##The reason why we used this is because that tensorflow has already udpated to 2.0 and many old API were no longer viable. 
##And the project will be implement in keras.
import math 
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy
from PIL import Image
from scipy import ndimage
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.framework import ops
from cnn_utils import *

np.random.seed(1)# Loading the data (signs)

##load dataset.
X_train_orig, Y_train_orig, X_test_orig, Y_test_orig, classes = load_dataset()

## Examine the shape of data
X_train = X_train_orig/255.
X_test = X_test_orig/255.
Y_train = convert_to_one_hot(Y_train_orig, 6).T
Y_test = convert_to_one_hot(Y_test_orig, 6).T
print ("The type of training sets = " + str(type(X_train)))
print ("number of training examples = " + str(X_train.shape[0]))
print ("number of test examples = " + str(X_test.shape[0]))
print ("X_train shape: " + str(X_train.shape))
print ("Y_train shape: " + str(Y_train.shape))
print ("X_test shape: " + str(X_test.shape))
print ("Y_test shape: " + str(Y_test.shape))
conv_layers = {}

## Create a model first for following layers
model = keras.models.Sequential()
##Accoding to original we should create function for initlizing weight and bias using xavier initlizer. But we can actually do it in keras with more elegent way now. 
## We will still keep the hyperparameter of original model where W1:[4,4,3,8] and W2:[2,2,8,16] for two conv2D layer.

##Add the first convoluted layers into the model.
model.add(keras.layers.Conv2D(8,4,1,padding="same",activation="relu",use_bias=True,kernel_initializer=keras.initializers.glorot_normal,bias_initializer="zeros"))
## Previous code completed weight bias initilization and computation towards both Z and A since activation was included. 

##Add pooling layer into model.
model.add(keras.layers.MaxPooling2D((8,8),8,padding="same"))
## This code will create a window for 8,8 and stride 8 pooling layer.

##Add second conv layer
model.add(keras.layers.Conv2D(16,2,1,padding="same",activation='relu',use_bias = True,kernel_initializer=keras.initializers.glorot_normal,bias_initializer="zeros"))

##Add second pooling layer
model.add(keras.layers.MaxPooling2D((4,4),4,padding="same"))

##Add flatten layer
model.add(keras.layers.Flatten())
##Add dense(FC) layer,
model.add(keras.layers.Dense(6))

model.compile(loss="sparse_categorical_crossentropy",
             optimizer = "Adam"),
              metrics=["accuracy"]
             )