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

dataset_inter1 = []
mf = open('boulware_new.csv','r')
for line in mf.readlines():
    val = line.split()
    for i in val:
        i = float(i)
    dataset_inter1.append(val)
dataset_inter1 = np.array(dataset_inter1)

dataset_inter2 = []
mp = open('conceder_new.csv','r')
for line in mp.readlines():
    val = line.split()
    for i in val:
        i = float(i)
    dataset_inter2.append(val)
dataset_inter2 = np.array(dataset_inter2)

dataset_inter3 = []
mp = open('fire10.csv','r')
for line in mp.readlines():
    val = line.split()
    for i in val:
        i = float(i)
    dataset_inter3.append(val)
dataset_inter3 = np.array(dataset_inter3)

dataset_inter = []
dataset_inter = np.vstack((dataset_inter1, dataset_inter2))
#dataset_inter = np.vstack((dataset_inter, dataset_inter3))

dataset = []
dataset = np.array(dataset_inter3)
print dataset.shape

dataset = dataset.astype('float32')
plt.plot(dataset)
plt.show()

dataset = pad_sequences(dataset, maxlen=max_sen_len)
np.random.seed(7)

# np.random.shuffle(dataset)
dataset = np.reshape(dataset, (dataset.shape[0], dataset.shape[1], 1))

#################################
# split into train and test sets
val_split = 0.999
train_size = int(len(dataset) * (1.0 - val_split))
test_size = len(dataset) - train_size

train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]

x_train = train[:,:-1]
y_train = train[:,1:]

x_test = test[:,:-1]
y_test = test[:,1:]
#################################

#x, y = dataset[:,:-1], dataset[:,1:]

model = Sequential()
model.add (LSTM (1, input_shape = (99,1), return_sequences=True, stateful=False, dtype='float32', dropout=0.3, recurrent_dropout=0.3))
model.compile(loss="mse", optimizer="adam", metrics=['accuracy'])
#model.fit(x,y,batch_size=1,epochs=20,validation_split=0.2,shuffle=True)
model.fit (x_train, y_train, batch_size=1, epochs=20, validation_data=(x_test, y_test), shuffle=True)