import numpy as np

dir_list = [ 'Data_20_2hyp/', 'Data_50_2hyp/', 'Data_100_2hyp/' ]
# Iterate through dir_list using dir_name
for dir_name in dir_list:

	fire2 = np.load(str(dir_name + 'Outputs/res_fire2.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
	fire5 = np.load(str(dir_name + 'Outputs/res_fire5.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
	fire10 = np.load(str(dir_name + 'Outputs/res_fire10.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
	fire20 = np.load(str(dir_name + 'Outputs/res_fire20.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
	fire50 = np.load(str(dir_name + 'Outputs/res_fire50.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]

	# intervals - halfs with open lower bound and closed upper bound
	# [0 - 0.5] -- 0.5
	# (0.5 - 1.0] -- 1.0

	prob_list_fire2 = []
	prob_list_fire5 = []
	prob_list_fire10 = []
	prob_list_fire20 = []
	prob_list_fire50 = []

	for i in xrange(100):

		# classes: 1,2 COUNTS
		c1_fire2 = 1
		c2_fire2 = 1
		total_fire2 = 2
		prob_fire2 = []

		c1_fire5 = 1
		c2_fire5 = 1
		total_fire5 = 2
		prob_fire5 = []

		c1_fire10 = 1
		c2_fire10 = 1
		total_fire10 = 2
		prob_fire10 = []

		c1_fire20 = 1
		c2_fire20 = 1
		total_fire20 = 2
		prob_fire20 = []

		c1_fire50 = 1
		c2_fire50 = 1
		total_fire50 = 2
		prob_fire50 = []

		for j in xrange(99):

			if fire2[i][j] <= 0.5:
				fire2[i][j] = 0.5
				c1_fire2 += 1
			elif fire2[i][j] <= 1.0:
				fire2[i][j] = 1.0
				c2_fire2 += 1
			total_fire2 += 1
			prob_fire2.append(float(c1_fire2)/total_fire2)
			prob_fire2.append(float(c2_fire2)/total_fire2)

			if fire5[i][j] <= 0.5:
				fire5[i][j] = 0.5
				c1_fire5 += 1
			elif fire5[i][j] <= 1.0:
				fire5[i][j] = 1.0
				c2_fire5 += 1
			total_fire5 += 1
			prob_fire5.append(float(c1_fire5)/total_fire5)
			prob_fire5.append(float(c2_fire5)/total_fire5)

			if fire10[i][j] <= 0.5:
				fire10[i][j] = 0.5
				c1_fire10 += 1
			elif fire10[i][j] <= 1.0:
				fire10[i][j] = 1.0
				c2_fire10 += 1
			total_fire10 += 1
			prob_fire10.append(float(c1_fire10)/total_fire10)
			prob_fire10.append(float(c2_fire10)/total_fire10)

			if fire20[i][j] <= 0.5:
				fire20[i][j] = 0.5
				c1_fire20 += 1
			elif fire20[i][j] <= 1.0:
				fire20[i][j] = 1.0
				c2_fire20 += 1
			total_fire20 += 1
			prob_fire20.append(float(c1_fire20)/total_fire20)
			prob_fire20.append(float(c2_fire20)/total_fire20)

			if fire50[i][j] <= 0.5:
				fire50[i][j] = 0.5
				c1_fire50 += 1
			elif fire50[i][j] <= 1.0:
				fire50[i][j] = 1.0
				c2_fire50 += 1
			total_fire50 += 1
			prob_fire50.append(float(c1_fire50)/total_fire50)
			prob_fire50.append(float(c2_fire50)/total_fire50)
			
		prob_list_fire2.append(prob_fire2)
		prob_list_fire5.append(prob_fire5)
		prob_list_fire10.append(prob_fire10)
		prob_list_fire20.append(prob_fire20)
		prob_list_fire50.append(prob_fire50)

	prob_list_fire2 = np.array(prob_list_fire2)
	prob_list_fire5 = np.array(prob_list_fire5)
	prob_list_fire10 = np.array(prob_list_fire10)
	prob_list_fire20 = np.array(prob_list_fire20)
	prob_list_fire50 = np.array(prob_list_fire50)

	np.savetxt(str(dir_name + "Class_Output_Probs/res_fire2.csv"), prob_list_fire2, delimiter=",")
	np.savetxt(str(dir_name + "Class_Output_Probs/res_fire5.csv"), prob_list_fire5, delimiter=",")
	np.savetxt(str(dir_name + "Class_Output_Probs/res_fire10.csv"), prob_list_fire10, delimiter=",")
	np.savetxt(str(dir_name + "Class_Output_Probs/res_fire20.csv"), prob_list_fire20, delimiter=",")
	np.savetxt(str(dir_name + "Class_Output_Probs/res_fire50.csv"), prob_list_fire50, delimiter=",")