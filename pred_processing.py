import numpy as np

# boul1 = np.fromfile('Data/Predictions/pred_boul1.npy', dtype=float, count=-1, sep='')
# conc1 = np.fromfile('Data/Predictions/pred_conc1.npy', dtype=float, count=-1, sep='')
# fire1 = np.fromfile('Data/Predictions/pred_fire1.npy', dtype=float, count=-1, sep='')

boul1 = np.load('Data/Predictions/pred_boul1.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
boul2 = np.load('Data/Predictions/pred_boul2.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
boul5 = np.load('Data/Predictions/pred_boul5.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
boul10 = np.load('Data/Predictions/pred_boul10.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
boul20 = np.load('Data/Predictions/pred_boul20.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
boul50 = np.load('Data/Predictions/pred_boul50.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]

conc1 = np.load('Data/Predictions/pred_conc1.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
conc2 = np.load('Data/Predictions/pred_conc2.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
conc5 = np.load('Data/Predictions/pred_conc5.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
conc10 = np.load('Data/Predictions/pred_conc10.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
conc20 = np.load('Data/Predictions/pred_conc20.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
conc50 = np.load('Data/Predictions/pred_conc50.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]

fire1 = np.load('Data/Predictions/pred_fire1.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
fire2 = np.load('Data/Predictions/pred_fire2.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
fire5 = np.load('Data/Predictions/pred_fire5.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
fire10 = np.load('Data/Predictions/pred_fire10.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
fire20 = np.load('Data/Predictions/pred_fire20.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
fire50 = np.load('Data/Predictions/pred_fire50.npy', mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]


# intervals - quartiles with open lower bound and closed upper bound
# [0 - 0.25] -- 0.25
# (0.25 - 0.5] -- 0.5
# (0.5 - 0.75] -- 0.75
# (0.75 - 1.0] -- 1.0

for i in xrange(100):
	for j in xrange(99):
		if boul1[i][j] <= 0.25:
			boul1[i][j] = 0.25
		elif boul1[i][j] <= 0.5:
			boul1[i][j] = 0.5
		elif boul1[i][j] <= 0.75:
			boul1[i][j] = 0.75
		elif boul1[i][j] <= 1.0:
			boul1[i][j] = 1.0

		if boul2[i][j] <= 0.25:
			boul2[i][j] = 0.25
		elif boul2[i][j] <= 0.5:
			boul2[i][j] = 0.5
		elif boul2[i][j] <= 0.75:
			boul2[i][j] = 0.75
		elif boul2[i][j] <= 1.0:
			boul2[i][j] = 1.0

		if boul5[i][j] <= 0.25:
			boul5[i][j] = 0.25
		elif boul5[i][j] <= 0.5:
			boul5[i][j] = 0.5
		elif boul5[i][j] <= 0.75:
			boul5[i][j] = 0.75
		elif boul5[i][j] <= 1.0:
			boul5[i][j] = 1.0

		if boul10[i][j] <= 0.25:
			boul10[i][j] = 0.25
		elif boul10[i][j] <= 0.5:
			boul10[i][j] = 0.5
		elif boul10[i][j] <= 0.75:
			boul10[i][j] = 0.75
		elif boul10[i][j] <= 1.0:
			boul10[i][j] = 1.0

		if boul20[i][j] <= 0.25:
			boul20[i][j] = 0.25
		elif boul20[i][j] <= 0.5:
			boul20[i][j] = 0.5
		elif boul20[i][j] <= 0.75:
			boul20[i][j] = 0.75
		elif boul20[i][j] <= 1.0:
			boul20[i][j] = 1.0

		if boul50[i][j] <= 0.25:
			boul50[i][j] = 0.25
		elif boul50[i][j] <= 0.5:
			boul50[i][j] = 0.5
		elif boul50[i][j] <= 0.75:
			boul50[i][j] = 0.75
		elif boul50[i][j] <= 1.0:
			boul50[i][j] = 1.0

		##########################

		if conc1[i][j] <= 0.25:
			conc1[i][j] = 0.25
		elif conc1[i][j] <= 0.5:
			conc1[i][j] = 0.5
		elif conc1[i][j] <= 0.75:
			conc1[i][j] = 0.75
		elif conc1[i][j] <= 1.0:
			conc1[i][j] = 1.0

		if conc2[i][j] <= 0.25:
			conc2[i][j] = 0.25
		elif conc2[i][j] <= 0.5:
			conc2[i][j] = 0.5
		elif conc2[i][j] <= 0.75:
			conc2[i][j] = 0.75
		elif conc2[i][j] <= 1.0:
			conc2[i][j] = 1.0

		if conc5[i][j] <= 0.25:
			conc5[i][j] = 0.25
		elif conc5[i][j] <= 0.5:
			conc5[i][j] = 0.5
		elif conc5[i][j] <= 0.75:
			conc5[i][j] = 0.75
		elif conc5[i][j] <= 1.0:
			conc5[i][j] = 1.0

		if conc10[i][j] <= 0.25:
			conc10[i][j] = 0.25
		elif conc10[i][j] <= 0.5:
			conc10[i][j] = 0.5
		elif conc10[i][j] <= 0.75:
			conc10[i][j] = 0.75
		elif conc10[i][j] <= 1.0:
			conc10[i][j] = 1.0

		if conc20[i][j] <= 0.25:
			conc20[i][j] = 0.25
		elif conc20[i][j] <= 0.5:
			conc20[i][j] = 0.5
		elif conc20[i][j] <= 0.75:
			conc20[i][j] = 0.75
		elif conc20[i][j] <= 1.0:
			conc20[i][j] = 1.0

		if conc50[i][j] <= 0.25:
			conc50[i][j] = 0.25
		elif conc50[i][j] <= 0.5:
			conc50[i][j] = 0.5
		elif conc50[i][j] <= 0.75:
			conc50[i][j] = 0.75
		elif conc50[i][j] <= 1.0:
			conc50[i][j] = 1.0

		##########################

		if fire1[i][j] <= 0.25:
			fire1[i][j] = 0.25
		elif fire1[i][j] <= 0.5:
			fire1[i][j] = 0.5
		elif fire1[i][j] <= 0.75:
			fire1[i][j] = 0.75
		elif fire1[i][j] <= 1.0:
			fire1[i][j] = 1.0

		if fire2[i][j] <= 0.25:
			fire2[i][j] = 0.25
		elif fire2[i][j] <= 0.5:
			fire2[i][j] = 0.5
		elif fire2[i][j] <= 0.75:
			fire2[i][j] = 0.75
		elif fire2[i][j] <= 1.0:
			fire2[i][j] = 1.0

		if fire5[i][j] <= 0.25:
			fire5[i][j] = 0.25
		elif fire5[i][j] <= 0.5:
			fire5[i][j] = 0.5
		elif fire5[i][j] <= 0.75:
			fire5[i][j] = 0.75
		elif fire5[i][j] <= 1.0:
			fire5[i][j] = 1.0

		if fire10[i][j] <= 0.25:
			fire10[i][j] = 0.25
		elif fire10[i][j] <= 0.5:
			fire10[i][j] = 0.5
		elif fire10[i][j] <= 0.75:
			fire10[i][j] = 0.75
		elif fire10[i][j] <= 1.0:
			fire10[i][j] = 1.0

		if fire20[i][j] <= 0.25:
			fire20[i][j] = 0.25
		elif fire20[i][j] <= 0.5:
			fire20[i][j] = 0.5
		elif fire20[i][j] <= 0.75:
			fire20[i][j] = 0.75
		elif fire20[i][j] <= 1.0:
			fire20[i][j] = 1.0

		if fire50[i][j] <= 0.25:
			fire50[i][j] = 0.25
		elif fire50[i][j] <= 0.5:
			fire50[i][j] = 0.5
		elif fire50[i][j] <= 0.75:
			fire50[i][j] = 0.75
		elif fire50[i][j] <= 1.0:
			fire50[i][j] = 1.0

np.savetxt("Data/Class_Predictions/pred_boul1.csv", boul1, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_boul2.csv", boul2, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_boul5.csv", boul5, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_boul10.csv", boul10, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_boul20.csv", boul20, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_boul50.csv", boul50, delimiter=",")

# np.savetxt("Data/Class_Predictions/pred_conc1.csv", conc1, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_conc2.csv", conc2, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_conc5.csv", conc5, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_conc10.csv", conc10, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_conc20.csv", conc20, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_conc50.csv", conc50, delimiter=",")

# np.savetxt("Data/Class_Predictions/pred_fire1.csv", fire1, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_fire2.csv", fire2, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_fire5.csv", fire5, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_fire10.csv", fire10, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_fire20.csv", fire20, delimiter=",")
# np.savetxt("Data/Class_Predictions/pred_fire50.csv", fire50, delimiter=",")

