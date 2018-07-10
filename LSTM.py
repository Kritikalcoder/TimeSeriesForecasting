import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cPickle
from collections import defaultdict
import re

import sys
import os
import math

os.environ['KERAS_BACKEND']='tensorflow'

from keras.preprocessing.sequence import pad_sequences
from keras.layers import LSTM, Dense
from keras.models import Sequential
from sklearn.metrics import mean_squared_error

import matplotlib

max_sen_len = 100
#val_split = 0.2

dataset_inter = []
mf = open('boulware.csv','r')
for line in mf.readlines():
    val = line.split()
    for i in val:
        i = float(i)
    dataset_inter.append(val)

dataset = []
dataset = np.array(dataset_inter)

dataset = dataset.astype('float32')
plt.plot(dataset)
plt.show()

# range of predicted rv values lies between 0 and 1
dataset = pad_sequences(dataset, maxlen=max_sen_len)
# fix random seed for reproducibility
np.random.seed(7)

# split into train and test sets
# train_size = int(len(dataset) * (1.0 - val_split))
# test_size = len(dataset) - train_size
# SHUFFLE DATASET USING NP SEED HERE 
np.random.shuffle(dataset)
print dataset.shape
dataset = np.reshape(dataset, (dataset.shape[0], dataset.shape[1], 1))
print dataset.shape
x, y = dataset[:,:-1], dataset[:,1:]
print x.shape
print y.shape
# train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]

# x_train = train[:,:-1]
# y_train = train[:,1:]

# x_test = test[:,:-1]
# y_test = test[:,1:]

# x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
# x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1)) 

# print x_train.shape
# print y_train.shape
# print x_test.shape
# print y_test.shape


model = Sequential()
#model.add (LSTM (10, input_shape = (max_sen_len,1), '''output_dim=99,''' activation='tanh', return_sequences=True, stateful=False, dtype='float32'))
model.add (LSTM (1, input_shape = (99,1), return_sequences=True, stateful=False, dtype='float32'))
# This is the part which I am not understanding

 
#model.add (Dense (1, output_dim=99, activation='sigmoid'))
#model.add (Dense (99, input_shape = (99,1), activation='sigmoid'))
model.compile(loss="mse", optimizer="adam", metrics=['accuracy'])

#model.fit (x_train, y_train, batch_size=1, epochs=100, validation_data=(x_test, y_test), shuffle=False)
model.fit(x,y,batch_size=1,epochs=100,validation_split=0.1,shuffle=True)
#model.fit (x_train, y_train, batch_size=512, nb_epoch=100, validation_data=(x_test, y_test), shuffle=False)

#score, acc = model.evaluate(x_test, y_test, batch_size=10, verbose=1)
#Predict each timestep given the last sequence of true data, in effect only predicting 1 step ahead each time
# predicted = model.predict(data)
# predicted = np.reshape(predicted, (predicted.size,))
# print predictedx
# test test