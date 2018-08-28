import numpy as np
import csv

dir_list = [ 'Data_20_4hyp/', 'Data_50_4hyp/', 'Data_100_4hyp/' ] 
# Iterate through dir_list using dir_name

for dir_name in dir_list:

	print (str(dir_name))

	fire2_out = np.load(str(dir_name + 'Outputs/res_fire2.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,-1]
	fire5_out = np.load(str(dir_name + 'Outputs/res_fire5.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,-1]
	fire10_out = np.load(str(dir_name + 'Outputs/res_fire10.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,-1]
	fire20_out = np.load(str(dir_name + 'Outputs/res_fire20.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,-1]
	fire50_out = np.load(str(dir_name + 'Outputs/res_fire50.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,-1]

	fire2 = np.load(str(dir_name + 'Preds/pred_fire2.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
	fire5 = np.load(str(dir_name + 'Preds/pred_fire5.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
	fire10 = np.load(str(dir_name + 'Preds/pred_fire10.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
	fire20 = np.load(str(dir_name + 'Preds/pred_fire20.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]
	fire50 = np.load(str(dir_name + 'Preds/pred_fire50.npy'), mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII').reshape(300,99)[0:100,:]

	######################

	prob_list_fire2 = []
	prob_list_fire5 = []
	prob_list_fire10 = []
	prob_list_fire20 = []
	prob_list_fire50 = []

	for i in xrange(100):

		# classes: 1,2,3,4 COUNTS
		c1_fire2 = 1
		c2_fire2 = 1
		c3_fire2 = 1
		c4_fire2 = 1
		total_fire2 = 4
		prob_fire2 = []

		c1_fire5 = 1
		c2_fire5 = 1
		c3_fire5 = 1
		c4_fire5 = 1
		total_fire5 = 4
		prob_fire5 = []

		c1_fire10 = 1
		c2_fire10 = 1
		c3_fire10 = 1
		c4_fire10 = 1
		total_fire10 = 4
		prob_fire10 = []

		c1_fire20 = 1
		c2_fire20 = 1
		c3_fire20 = 1
		c4_fire20 = 1
		total_fire20 = 4
		prob_fire20 = []

		c1_fire50 = 1
		c2_fire50 = 1
		c3_fire50 = 1
		c4_fire50 = 1
		total_fire50 = 4
		prob_fire50 = []

		for j in xrange(99):

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

		prob_list_fire2.append(prob_fire2)
		prob_list_fire5.append(prob_fire5)
		prob_list_fire10.append(prob_fire10)
		prob_list_fire20.append(prob_fire20)
		prob_list_fire50.append(prob_fire50)

	prob_list_fire2 = np.array(prob_list_fire2)[0:100,-4:]
	prob_list_fire5 = np.array(prob_list_fire5)[0:100,-4:]
	prob_list_fire10 = np.array(prob_list_fire10)[0:100,-4:]
	prob_list_fire20 = np.array(prob_list_fire20)[0:100,-4:]
	prob_list_fire50 = np.array(prob_list_fire50)[0:100,-4:]

	fire2_pred = []
	fire5_pred = []
	fire10_pred = []
	fire20_pred = []
	fire50_pred = []

	for index in xrange(100) :
		fire2_pred.append(prob_list_fire2[index][0] * 0.12 + prob_list_fire2[index][1] * 0.321 + prob_list_fire2[index][2] * 0.57 + prob_list_fire2[index][3] * 0.75)
		fire5_pred.append(prob_list_fire5[index][0] * 0.12 + prob_list_fire5[index][1] * 0.321 + prob_list_fire5[index][2] * 0.57 + prob_list_fire5[index][3] * 0.75)
		fire10_pred.append(prob_list_fire10[index][0] * 0.12 + prob_list_fire10[index][1] * 0.321 + prob_list_fire10[index][2] * 0.57 + prob_list_fire10[index][3] * 0.75)
		fire20_pred.append(prob_list_fire20[index][0] * 0.12 + prob_list_fire20[index][1] * 0.321 + prob_list_fire20[index][2] * 0.57 + prob_list_fire20[index][3] * 0.75)
		fire50_pred.append(prob_list_fire50[index][0] * 0.12 + prob_list_fire50[index][1] * 0.321 + prob_list_fire50[index][2] * 0.57 + prob_list_fire50[index][3] * 0.75)
		
	fire2_pred = np.array(fire2_pred)
	fire5_pred = np.array(fire5_pred)
	fire10_pred = np.array(fire10_pred)
	fire20_pred = np.array(fire20_pred)
	fire50_pred = np.array(fire50_pred)

	####################################

	fire2_diff = []
	fire5_diff = []
	fire10_diff = []
	fire20_diff = []
	fire50_diff = []

	for index in xrange(100) :
		fire2_diff.append(float(fire2_out[index] - fire2_pred[index]))
		fire5_diff.append(float(fire5_out[index] - fire5_pred[index]))
		fire10_diff.append(float(fire10_out[index] - fire10_pred[index]))
		fire20_diff.append(float(fire20_out[index] - fire20_pred[index]))
		fire50_diff.append(float(fire50_out[index] - fire50_pred[index]))

	fire2_diff = np.array(fire2_diff)
	fire5_diff = np.array(fire5_diff)
	fire10_diff = np.array(fire10_diff)
	fire20_diff = np.array(fire20_diff)
	fire50_diff = np.array(fire50_diff)

	np.savetxt(str(dir_name + "Differences/diff2.csv"), fire2_diff, delimiter=",")
	np.savetxt(str(dir_name + "Differences/diff5.csv"), fire5_diff, delimiter=",")
	np.savetxt(str(dir_name + "Differences/diff10.csv"), fire10_diff, delimiter=",")
	np.savetxt(str(dir_name + "Differences/diff20.csv"), fire20_diff, delimiter=",")
	np.savetxt(str(dir_name + "Differences/diff50.csv"), fire50_diff, delimiter=",")

	print (np.average(fire2_diff))
	print (np.average(fire5_diff))
	print (np.average(fire10_diff))
	print (np.average(fire20_diff))
	print (np.average(fire50_diff))
