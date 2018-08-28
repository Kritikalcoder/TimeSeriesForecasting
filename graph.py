#informal graph plotting script

import numpy as np
import matplotlib.pyplot as plt

fire_output = np.load('Data_20_2hyp/Outputs/res_fire5.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
fire_pred = np.load('Data_20_2hyp/Preds/pred_fire5.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]

print fire_pred.shape
print fire_output.shape

x=[]
for i in xrange(0,99):
	x.append(i)
plt.figure('data')
plt.plot(x,fire_output[0])
plt.plot(x,fire_pred[0])

plt.plot(x,fire_output[10])
plt.plot(x,fire_pred[10])

plt.plot(x,fire_output[22])
plt.plot(x,fire_pred[22])


# for i in fire_output:
# 	plt.plot(x,i)
# for i in fire_pred:
# 	plt.plot(x,i)
plt.show()