import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cPickle
from collections import defaultdict
import sys, os, math, re
os.environ['KERAS_BACKEND']='tensorflow'
from keras.preprocessing.sequence import pad_sequences
from keras.layers import LSTM, Dense
from keras.models import Sequential
from sklearn.metrics import mean_squared_error
import matplotlib

max_sen_len = 100

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

dataset = pad_sequences(dataset, maxlen=max_sen_len)
np.random.seed(7)

np.random.shuffle(dataset)
dataset = np.reshape(dataset, (dataset.shape[0], dataset.shape[1], 1))
x, y = dataset[:,:-1], dataset[:,1:]

model = Sequential()
model.add (LSTM (1, input_shape = (99,1), return_sequences=True, stateful=False, dtype='float32'))
model.compile(loss="mse", optimizer="adam", metrics=['accuracy'])
model.fit(x,y,batch_size=1,epochs=100,validation_split=0.1,shuffle=True)