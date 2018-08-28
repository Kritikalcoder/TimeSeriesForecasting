### FIRE DOMAIN ONLY

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

from keras.models import model_from_json
from pandas import HDFStore 

max_sen_len = 100

#dir_list = [ 'Data_20_2hyp/', 'Data_20_4hyp/', 'Data_50_2hyp/', 'Data_50_4hyp/', 'Data_100_2hyp/', 'Data_100_4hyp/' ] 
dir_list = [ 'Data_50_2hyp/', 'Data_50_4hyp/', 'Data_100_2hyp/', 'Data_100_4hyp/' ] 

input_flist = [ 'Inputs/fire2.csv', 'Inputs/fire5.csv', 'Inputs/fire10.csv', 'Inputs/fire20.csv', 'Inputs/fire50.csv']
output_flist = [ 'Outputs/res_fire2.npy', 'Outputs/res_fire5.npy', 'Outputs/res_fire10.npy', 'Outputs/res_fire20.npy', 'Outputs/res_fire50.npy']
preds_flist = [ 'Preds/pred_fire2.npy', 'Preds/pred_fire5.npy', 'Preds/pred_fire10.npy', 'Preds/pred_fire20.npy', 'Preds/pred_fire50.npy']

# Iterate through dir_list using dir_name
# Iterate through input_flist using input_fname
# Iterate through output_flist using output_fname
# Iterate through preds_flist using preds_fname

for dir_name in dir_list:

	for index_ in xrange(5):

		if dir_name == 'Data_50_2hyp/' and index_ == 0:
			continue
		if dir_name == 'Data_50_2hyp/' and index_ == 1:
			continue
		input_fname = input_flist[index_]
		output_fname = output_flist[index_]
		preds_fname = preds_flist[index_]

		print (str (dir_name + input_fname))

		dataset_inter = []
		ms = open(str(dir_name + input_fname),'r')
		for line in ms.readlines():
		    val = line.split()
		    val = [float(i) for i in val]
		    dataset_inter.append(val)
		dataset_inter = np.array(dataset_inter)

		dataset = []
		dataset = np.array(dataset_inter)
		dataset = dataset.astype('float32')

		# x=[]
		# for i in xrange(0,100):
		# 	x.append(i)
		# plt.figure('data')
		# for i in dataset:
		# 	plt.plot(x,i)
		# plt.show()

		np.random.seed(7)
		# np.random.shuffle(dataset)
		dataset = np.reshape(dataset, (dataset.shape[0], dataset.shape[1], 1))

		#################################
		# split into train and test sets
		val_split = 0.3
		train_size = int(len(dataset) * (1.0 - val_split))
		test_size = len(dataset) - train_size

		train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]

		x_train = train[:,:-1]
		y_train = train[:,1:]

		x_test = test[:,:-1]
		y_test = test[:,1:]
		#################################

		#x, y = dataset[:,:-1], dataset[:,1:]

		############### change model from sequence prediction to last value prediction ###################

		y_train_last = [[y_train[i,-1] for j in xrange(0,y_train.shape[1])] for i in xrange(0,y_train.shape[0])]

		y_test_last = [[y_test[i,-1] for j in xrange(0,y_test.shape[1])] for i in xrange(0,y_test.shape[0])]

		y_train_last = np.array(y_train_last)
		y_test_last = np.array(y_test_last)

		###################################################################################################

		model = Sequential()
		model.add (LSTM (1, input_shape = (99,1), return_sequences=True, stateful=False, dtype='float32', dropout=0.3, recurrent_dropout=0.3))
		model.compile(loss="mse", optimizer="adam", metrics=['accuracy'])
		# model.fit (x_train, y_train, batch_size=1, epochs=20, validation_data=(x_test, y_test), shuffle=True)
		model.fit (x_train, y_train_last, batch_size=1, epochs=10, validation_data=(x_test, y_test_last), shuffle=True)
		predictions = model.predict(x_test)

		with open(str(dir_name + preds_fname),'wb') as pr: 
			np.save(pr,predictions)

		with open(str(dir_name + output_fname),'wb') as res: 
			np.save(res,y_test_last)

		# a = np.load(fp)

		# serialize model to JSON

		'''
		model_json = model.to_json()
		with open("model_fire10.json", "w") as json_file:
		    json_file.write(model_json)
		# serialize weights to HDF5

		'''

		# ######## model.save_weights("model_boul10.h5")
		# print("Saved model to disk")
		 
		# later...x
		 
		# # load json and create model
		# json_file = open('model_boul10.json', 'r')
		# loaded_model_json = json_file.read()
		# json_file.close()
		# loaded_model = model_from_json(loaded_model_json)
		# # load weights into new model
		# loaded_model.load_weights("model_boul10.h5")
		# print("Loaded model from disk")
		 
		# # evaluate loaded model on test data
		# loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
		# score = loaded_model.evaluate(X, Y, verbose=0)
		# print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))