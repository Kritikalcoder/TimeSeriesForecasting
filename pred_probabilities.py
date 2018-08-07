import numpy as np

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

prob_list_boul1 = []
prob_list_boul2 = []
prob_list_boul5 = []
prob_list_boul10 = []
prob_list_boul20 = []
prob_list_boul50 = []

prob_list_conc1 = []
prob_list_conc2 = []
prob_list_conc5 = []
prob_list_conc10 = []
prob_list_conc20 = []
prob_list_conc50 = []

prob_list_fire1 = []
prob_list_fire2 = []
prob_list_fire5 = []
prob_list_fire10 = []
prob_list_fire20 = []
prob_list_fire50 = []

for i in xrange(100):

	# classes: 1,2,3,4 COUNTS
	c1_boul1 = 1
	c2_boul1 = 1
	c3_boul1 = 1
	c4_boul1 = 1
	total_boul1 = 4
	prob_boul1 = []

	# classes: 1,2,3,4 COUNTS
	c1_boul2 = 1
	c2_boul2 = 1
	c3_boul2 = 1
	c4_boul2 = 1
	total_boul2 = 4
	prob_boul2 = []

	# classes: 1,2,3,4 COUNTS
	c1_boul5 = 1
	c2_boul5 = 1
	c3_boul5 = 1
	c4_boul5 = 1
	total_boul5 = 4
	prob_boul5 = []

	# classes: 1,2,3,4 COUNTS
	c1_boul10 = 1
	c2_boul10 = 1
	c3_boul10 = 1
	c4_boul10 = 1
	total_boul10 = 4
	prob_boul10 = []

	# classes: 1,2,3,4 COUNTS
	c1_boul20 = 1
	c2_boul20 = 1
	c3_boul20 = 1
	c4_boul20 = 1
	total_boul20 = 4
	prob_boul20 = []

	# classes: 1,2,3,4 COUNTS
	c1_boul50 = 1
	c2_boul50 = 1
	c3_boul50 = 1
	c4_boul50 = 1
	total_boul50 = 4
	prob_boul50 = []

	########################################

	# classes: 1,2,3,4 COUNTS
	c1_conc1 = 1
	c2_conc1 = 1
	c3_conc1 = 1
	c4_conc1 = 1
	total_conc1 = 4
	prob_conc1 = []

	# classes: 1,2,3,4 COUNTS
	c1_conc2 = 1
	c2_conc2 = 1
	c3_conc2 = 1
	c4_conc2 = 1
	total_conc2 = 4
	prob_conc2 = []

	# classes: 1,2,3,4 COUNTS
	c1_conc5 = 1
	c2_conc5 = 1
	c3_conc5 = 1
	c4_conc5 = 1
	total_conc5 = 4
	prob_conc5 = []

	# classes: 1,2,3,4 COUNTS
	c1_conc10 = 1
	c2_conc10 = 1
	c3_conc10 = 1
	c4_conc10 = 1
	total_conc10 = 4
	prob_conc10 = []

	# classes: 1,2,3,4 COUNTS
	c1_conc20 = 1
	c2_conc20 = 1
	c3_conc20 = 1
	c4_conc20 = 1
	total_conc20 = 4
	prob_conc20 = []

	# classes: 1,2,3,4 COUNTS
	c1_conc50 = 1
	c2_conc50 = 1
	c3_conc50 = 1
	c4_conc50 = 1
	total_conc50 = 4
	prob_conc50 = []

	##############################


	# classes: 1,2,3,4 COUNTS
	c1_fire1 = 1
	c2_fire1 = 1
	c3_fire1 = 1
	c4_fire1 = 1
	total_fire1 = 4
	prob_fire1 = []

	# classes: 1,2,3,4 COUNTS
	c1_fire2 = 1
	c2_fire2 = 1
	c3_fire2 = 1
	c4_fire2 = 1
	total_fire2 = 4
	prob_fire2 = []

	# classes: 1,2,3,4 COUNTS
	c1_fire5 = 1
	c2_fire5 = 1
	c3_fire5 = 1
	c4_fire5 = 1
	total_fire5 = 4
	prob_fire5 = []

	# classes: 1,2,3,4 COUNTS
	c1_fire10 = 1
	c2_fire10 = 1
	c3_fire10 = 1
	c4_fire10 = 1
	total_fire10 = 4
	prob_fire10 = []

	# classes: 1,2,3,4 COUNTS
	c1_fire20 = 1
	c2_fire20 = 1
	c3_fire20 = 1
	c4_fire20 = 1
	total_fire20 = 4
	prob_fire20 = []

	# classes: 1,2,3,4 COUNTS
	c1_fire50 = 1
	c2_fire50 = 1
	c3_fire50 = 1
	c4_fire50 = 1
	total_fire50 = 4
	prob_fire50 = []


	########################



	for j in xrange(99):
		if boul1[i][j] <= 0.25:
			boul1[i][j] = 0.25
			c1_boul1 += 1
		elif boul1[i][j] <= 0.5:
			boul1[i][j] = 0.5
			c2_boul1 += 1
		elif boul1[i][j] <= 0.75:
			boul1[i][j] = 0.75
			c3_boul1 += 1
		elif boul1[i][j] <= 1.0:
			boul1[i][j] = 1.0
			c4_boul1 += 1
		total_boul1 += 1
		prob_boul1.append([c1_boul1/total_boul1, c2_boul1/total_boul1, c3_boul1/total_boul1, c4_boul1/total_boul1])

		if boul2[i][j] <= 0.25:
			boul2[i][j] = 0.25
			c1_boul2 += 1
		elif boul2[i][j] <= 0.5:
			boul2[i][j] = 0.5
			c2_boul2 += 1
		elif boul2[i][j] <= 0.75:
			boul2[i][j] = 0.75
			c3_boul2 += 1
		elif boul2[i][j] <= 1.0:
			boul2[i][j] = 1.0
			c4_boul2 += 1
		total_boul2 += 1
		prob_boul2.append([c1_boul2/total_boul2, c2_boul2/total_boul2, c3_boul2/total_boul2, c4_boul2/total_boul2])


		if boul5[i][j] <= 0.25:
			boul5[i][j] = 0.25
			c1_boul5 += 1
		elif boul5[i][j] <= 0.5:
			boul5[i][j] = 0.5
			c2_boul5 += 1
		elif boul5[i][j] <= 0.75:
			boul5[i][j] = 0.75
			c3_boul5 += 1
		elif boul5[i][j] <= 1.0:
			boul5[i][j] = 1.0
			c4_boul5 += 1
		total_boul5 += 1
		prob_boul5.append([c1_boul5/total_boul5, c2_boul5/total_boul5, c3_boul5/total_boul5, c4_boul5/total_boul5])

		if boul10[i][j] <= 0.25:
			boul10[i][j] = 0.25
			c1_boul10 += 1
		elif boul10[i][j] <= 0.5:
			boul10[i][j] = 0.5
			c2_boul10 += 1
		elif boul10[i][j] <= 0.75:
			boul10[i][j] = 0.75
			c3_boul10 += 1
		elif boul10[i][j] <= 1.0:
			boul10[i][j] = 1.0
			c4_boul10 += 1
		total_boul10 += 1
		prob_boul10.append([c1_boul10/total_boul10, c2_boul10/total_boul10, c3_boul10/total_boul10, c4_boul10/total_boul10])

		if boul20[i][j] <= 0.25:
			boul20[i][j] = 0.25
			c1_boul20 += 1
		elif boul20[i][j] <= 0.5:
			boul20[i][j] = 0.5
			c2_boul20 += 1
		elif boul20[i][j] <= 0.75:
			boul20[i][j] = 0.75
			c3_boul20 += 1
		elif boul20[i][j] <= 1.0:
			boul20[i][j] = 1.0
			c4_boul20 += 1
		total_boul20 += 1
		prob_boul20.append([c1_boul20/total_boul20, c2_boul20/total_boul20, c3_boul20/total_boul20, c4_boul20/total_boul20])

		if boul50[i][j] <= 0.25:
			boul50[i][j] = 0.25
			c1_boul50 += 1
		elif boul50[i][j] <= 0.5:
			boul50[i][j] = 0.5
			c2_boul50 += 1
		elif boul50[i][j] <= 0.75:
			boul50[i][j] = 0.75
			c3_boul50 += 1
		elif boul50[i][j] <= 1.0:
			boul50[i][j] = 1.0
			c4_boul50 += 1
		total_boul50 += 1
		prob_boul50.append([c1_boul50/total_boul50, c2_boul50/total_boul50, c3_boul50/total_boul50, c4_boul50/total_boul50])

		##########################

		if conc1[i][j] <= 0.25:
			conc1[i][j] = 0.25
			c1_conc1 += 1
		elif conc1[i][j] <= 0.5:
			conc1[i][j] = 0.5
			c2_conc1 += 1
		elif conc1[i][j] <= 0.75:
			conc1[i][j] = 0.75
			c3_conc1 += 1
		elif conc1[i][j] <= 1.0:
			conc1[i][j] = 1.0
			c4_conc1 += 1
		total_conc1 += 1
		prob_conc1.append([c1_conc1/total_conc1, c2_conc1/total_conc1, c3_conc1/total_conc1, c4_conc1/total_conc1])

		if conc2[i][j] <= 0.25:
			conc2[i][j] = 0.25
			c1_conc2 += 1
		elif conc2[i][j] <= 0.5:
			conc2[i][j] = 0.5
			c2_conc2 += 1
		elif conc2[i][j] <= 0.75:
			conc2[i][j] = 0.75
			c3_conc2 += 1
		elif conc2[i][j] <= 1.0:
			conc2[i][j] = 1.0
			c4_conc2 += 1
		total_conc2 += 1
		prob_conc2.append([c1_conc2/total_conc2, c2_conc2/total_conc2, c3_conc2/total_conc2, c4_conc2/total_conc2])

		if conc5[i][j] <= 0.25:
			conc5[i][j] = 0.25
			c1_conc5 += 1
		elif conc5[i][j] <= 0.5:
			conc5[i][j] = 0.5
			c2_conc5 += 1
		elif conc5[i][j] <= 0.75:
			conc5[i][j] = 0.75
			c3_conc5 += 1
		elif conc5[i][j] <= 1.0:
			conc5[i][j] = 1.0
			c4_conc5 += 1
		total_conc5 += 1
		prob_conc5.append([c1_conc5/total_conc5, c2_conc5/total_conc5, c3_conc5/total_conc5, c4_conc5/total_conc5])

		if conc10[i][j] <= 0.25:
			conc10[i][j] = 0.25
			c1_conc10 += 1
		elif conc10[i][j] <= 0.5:
			conc10[i][j] = 0.5
			c2_conc10 += 1
		elif conc10[i][j] <= 0.75:
			conc10[i][j] = 0.75
			c3_conc10 += 1
		elif conc10[i][j] <= 1.0:
			conc10[i][j] = 1.0
			c4_conc10 += 1
		total_conc10 += 1
		prob_conc10.append([c1_conc10/total_conc10, c2_conc10/total_conc10, c3_conc10/total_conc10, c4_conc10/total_conc10])

		if conc20[i][j] <= 0.25:
			conc20[i][j] = 0.25
			c1_conc20 += 1
		elif conc20[i][j] <= 0.5:
			conc20[i][j] = 0.5
			c2_conc20 += 1
		elif conc20[i][j] <= 0.75:
			conc20[i][j] = 0.75
			c3_conc20 += 1
		elif conc20[i][j] <= 1.0:
			conc20[i][j] = 1.0
			c4_conc20 += 1
		total_conc20 += 1
		prob_conc20.append([c1_conc20/total_conc20, c2_conc20/total_conc20, c3_conc20/total_conc20, c4_conc20/total_conc20])

		if conc50[i][j] <= 0.25:
			conc50[i][j] = 0.25
			c1_conc50 += 1
		elif conc50[i][j] <= 0.5:
			conc50[i][j] = 0.5
			c2_conc50 += 1
		elif conc50[i][j] <= 0.75:
			conc50[i][j] = 0.75
			c3_conc50 += 1
		elif conc50[i][j] <= 1.0:
			conc50[i][j] = 1.0
			c4_conc50 += 1
		total_conc50 += 1
		prob_conc50.append([c1_conc50/total_conc50, c2_conc50/total_conc50, c3_conc50/total_conc50, c4_conc50/total_conc50])

		##########################

		if fire1[i][j] <= 0.25:
			fire1[i][j] = 0.25
			c1_fire1 += 1
		elif fire1[i][j] <= 0.5:
			fire1[i][j] = 0.5
			c2_fire1 += 1
		elif fire1[i][j] <= 0.75:
			fire1[i][j] = 0.75
			c3_fire1 += 1
		elif fire1[i][j] <= 1.0:
			fire1[i][j] = 1.0
			c4_fire1 += 1
		total_fire1 += 1
		prob_fire1.append(float(c1_fire1)/total_fire1)
		prob_fire1.append(float(c2_fire1)/total_fire1)
		prob_fire1.append(float(c3_fire1)/total_fire1)
		prob_fire1.append(float(c4_fire1)/total_fire1)

		if fire2[i][j] <= 0.25:
			fire2[i][j] = 0.25
			c1_fire2 += 1
		elif fire2[i][j] <= 0.5:
			fire2[i][j] = 0.5
			c2_fire2 += 1
		elif fire2[i][j] <= 0.75:
			fire2[i][j] = 0.75
			c3_fire2 += 1
		elif fire2[i][j] <= 1.0:
			fire2[i][j] = 1.0
			c4_fire2 += 1
		total_fire2 += 1
		prob_fire2.append(float(c1_fire2)/total_fire2)
		prob_fire2.append(float(c2_fire2)/total_fire2)
		prob_fire2.append(float(c3_fire2)/total_fire2)
		prob_fire2.append(float(c4_fire2)/total_fire2)
		# float("{0:.4f}".format(x))

		if fire5[i][j] <= 0.25:
			fire5[i][j] = 0.25
			c1_fire5 += 1
		elif fire5[i][j] <= 0.5:
			fire5[i][j] = 0.5
			c2_fire5 += 1
		elif fire5[i][j] <= 0.75:
			fire5[i][j] = 0.75
			c3_fire5 += 1
		elif fire5[i][j] <= 1.0:
			fire5[i][j] = 1.0
			c4_fire5 += 1
		total_fire5 += 1
		prob_fire5.append(float(c1_fire5)/total_fire5)
		prob_fire5.append(float(c2_fire5)/total_fire5)
		prob_fire5.append(float(c3_fire5)/total_fire5)
		prob_fire5.append(float(c4_fire5)/total_fire5)

		if fire10[i][j] <= 0.25:
			fire10[i][j] = 0.25
			c1_fire10 += 1
		elif fire10[i][j] <= 0.5:
			fire10[i][j] = 0.5
			c2_fire10 += 1
		elif fire10[i][j] <= 0.75:
			fire10[i][j] = 0.75
			c3_fire10 += 1
		elif fire10[i][j] <= 1.0:
			fire10[i][j] = 1.0
			c4_fire10 += 1
		total_fire10 += 1
		prob_fire10.append(float(c1_fire10)/total_fire10)
		prob_fire10.append(float(c2_fire10)/total_fire10)
		prob_fire10.append(float(c3_fire10)/total_fire10)
		prob_fire10.append(float(c4_fire10)/total_fire10)

		if fire20[i][j] <= 0.25:
			fire20[i][j] = 0.25
			c1_fire20 += 1
		elif fire20[i][j] <= 0.5:
			fire20[i][j] = 0.5
			c2_fire20 += 1
		elif fire20[i][j] <= 0.75:
			fire20[i][j] = 0.75
			c3_fire20 += 1
		elif fire20[i][j] <= 1.0:
			fire20[i][j] = 1.0
			c4_fire20 += 1
		total_fire20 += 1
		prob_fire20.append(float(c1_fire20)/total_fire20)
		prob_fire20.append(float(c2_fire20)/total_fire20)
		prob_fire20.append(float(c3_fire20)/total_fire20)
		prob_fire20.append(float(c4_fire20)/total_fire20)

		if fire50[i][j] <= 0.25:
			fire50[i][j] = 0.25
			c1_fire50 += 1
		elif fire50[i][j] <= 0.5:
			fire50[i][j] = 0.5
			c2_fire50 += 1
		elif fire50[i][j] <= 0.75:
			fire50[i][j] = 0.75
			c3_fire50 += 1
		elif fire50[i][j] <= 1.0:
			fire50[i][j] = 1.0
			c4_fire50 += 1
		total_fire50 += 1
		prob_fire50.append(float(c1_fire50)/total_fire50)
		prob_fire50.append(float(c2_fire50)/total_fire50)
		prob_fire50.append(float(c3_fire50)/total_fire50)
		prob_fire50.append(float(c4_fire50)/total_fire50)

	prob_list_boul1.append(prob_boul1)
	prob_list_boul2.append(prob_boul2)
	prob_list_boul5.append(prob_boul5)
	prob_list_boul10.append(prob_boul10)
	prob_list_boul20.append(prob_boul20)
	prob_list_boul50.append(prob_boul50)

	prob_list_conc1.append(prob_conc1)
	prob_list_conc2.append(prob_conc2)
	prob_list_conc5.append(prob_conc5)
	prob_list_conc10.append(prob_conc10)
	prob_list_conc20.append(prob_conc20)
	prob_list_conc50.append(prob_conc50)

	prob_list_fire1.append(prob_fire1)
	prob_list_fire2.append(prob_fire2)
	prob_list_fire5.append(prob_fire5)
	prob_list_fire10.append(prob_fire10)
	prob_list_fire20.append(prob_fire20)
	prob_list_fire50.append(prob_fire50)

prob_list_fire1 = np.array(prob_list_fire1)
prob_list_fire2 = np.array(prob_list_fire2)
prob_list_fire5 = np.array(prob_list_fire5)
prob_list_fire10 = np.array(prob_list_fire10)
prob_list_fire20 = np.array(prob_list_fire20)
prob_list_fire50 = np.array(prob_list_fire50)

# np.savetxt("Data/Class_Prediction_Probs/pred_fire1.csv", prob_list_fire1, delimiter=",")
np.savetxt("Data/Class_Prediction_Probs/pred_fire2.csv", prob_list_fire2, delimiter=",")
# np.savetxt("Data/Class_Prediction_Probs/pred_fire5.csv", prob_list_fire5, delimiter=",")
# np.savetxt("Data/Class_Prediction_Probs/pred_fire10.csv", prob_list_fire10, delimiter=",")
# np.savetxt("Data/Class_Prediction_Probs/pred_fire20.csv", prob_list_fire20, delimiter=",")
# np.savetxt("Data/Class_Prediction_Probs/pred_fire50.csv", prob_list_fire50, delimiter=",")