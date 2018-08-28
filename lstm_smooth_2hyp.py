import random
import numpy as np
import math
import numpy.polynomial.polynomial as poly
import matplotlib
import matplotlib.pyplot as plt
import operator
import matplotlib.backends.backend_pdf
from scipy.stats import *
import csv

########## Generating Utilities according to Tim Barslaag #########

def GenerateTimUtility( rv,rounds):
	l=[]
	l.append(rv);
	for i in range(1,rounds):
		l.append(float((l[i-1]+1)*(l[i-1]+1))/4)
	return l

###################################################################

def getflag(direction,Gridcoords,GridSize):
	flag=0
	if(direction==1):
		if(Gridcoords[0]!=0):
			Gridcoords[0]-=1                 ### Moving North
		if(Gridcoords[1]==GridSize-1):
			flag=3
		elif(Gridcoords[1]==0):
			flag=2
		elif(Gridcoords[0]+1==GridSize-1):
			flag=4
	elif(direction==2):
		if(Gridcoords[1]!=0):
			Gridcoords[1]-=1                 ### Moving West
		if(Gridcoords[0]==0):
			flag=1
		elif(Gridcoords[1]+1==GridSize-1):
			flag==3
		elif(Gridcoords[0]==GridSize-1):
			flag=4

	elif(direction==3):
		if(Gridcoords[1]!=GridSize-1):
			Gridcoords[1]+=1                 ### Moving East
		if(Gridcoords[0]==GridSize-1):
			flag=4
		elif(Gridcoords[0]==0):
			flag=1
		elif(Gridcoords[1]-1==0):
			flag=2
	else:
		if(Gridcoords[0]!=GridSize-1):
			Gridcoords[0]+=1                 ### Moving South
		if(Gridcoords[0]-1==0):
			flag=1
		elif(Gridcoords[1]==GridSize-1):
			flag=3
		elif(Gridcoords[1]==0):
			flag=2
	return flag
	
#############################################################
def Firerv(RV,roundnum,Deadline,UpdateRate,GridSize,Gridcoords):
	ManPower=[12,10,7,4]
	Utilities=[0.75,0.57,0.321,0.12]
	
	if(roundnum==0):
		# print "---round 1: =="
		direction=random.randint(1,4)
		# direction=random.choice([1,4])
		### Gridcoords Updation 
		flag=getflag(direction,Gridcoords,GridSize)
		# print "------"
		# print direction
		# print Gridcoords
		# print "------"
		if(flag==0 ):
			return Utilities[direction-1]
			#return getReservationUtility(ManPower[direction-1])

		else:	

			### commented by Kritika
			#print "This case: "+str(flag) + " "+ str(ManPower[direction-1] )
			###

			# return getReservationUtility( max (ManPower[flag-1], ManPower[direction-1] )) 
			return max (Utilities[flag-1], Utilities[direction-1] )

	elif(roundnum%UpdateRate==0):
		# print "---update == " + str(roundnum)   
		direction=random.randint(1,4)
		# direction=random.choice([1,4])
		flag=getflag(direction,Gridcoords,GridSize)
		# print "------"
		# print direction
		# print Gridcoords
		# print "------"
		if(flag==0 ):
			# return getReservationUtility(ManPower[direction-1])
			return Utilities[direction-1]

		else:	
			# print "This case: "+str(flag) + " "+ str(ManPower[direction-1] )
			# return getReservationUtility( max (ManPower[flag-1], ManPower[direction-1] ) )
			return Utilities[direction-1]

	else:
		return RV[len(RV)-1]


#############################################################

def getprobability( rows ):
	#probabilities=[[0.25,0.25,0.25,0.25]]
	probabilities=[[0.5,0.5]]
	cnt =0
	l=[]
	for i in rows:
		l.append(float(i))
		cnt=cnt+1
		if(cnt%2==0):
			probabilities.append(l)
			l=[]
	return probabilities


if __name__ == '__main__':


	Average_rv=[]
	AverageUtilities_Tims=[]
	AverageUtilities_lstm=[]

	####----- CSV parsing ---########3

	rows=[]
	fields=[]


	dir_list = [ 'Data_20_2hyp/', 'Data_50_2hyp/', 'Data_100_2hyp/' ]
	class_pred_probs_list = ['pred_fire2.csv', 'pred_fire5.csv', 'pred_fire10.csv', 'pred_fire20.csv', 'pred_fire50.csv', ]
	# update rate assumed to be same
	# grid size assumed to be same

	for dir_name in dir_list:
		for file_name in class_pred_probs_list:

			print (str(dir_name + "Class_Pred_Probs/" + file_name))

			with open(str(dir_name + "Class_Pred_Probs/" + file_name), 'r') as csvfile:
				csvreader = csv.reader(csvfile)
				fields = csvreader.next()
				for row in csvreader:
					rows.append(row)

			for iterations in xrange(1,100):
				probabilities=getprobability(rows[iterations-1])
				# probabilities=getprobability(rows[22])
				# print probabilities[1]

				RV=[0]
				Deadline = 100
				intervals=2
				UpdateRate=2     ##### keep updating the updaterate according to csv file parsed
				random_rv=[0.12,0.75]

				# iterations=1

				Utilities=[]
				actual_utility=[]

				for rv in random_rv:
						Utilities.append(GenerateTimUtility(rv,Deadline))
						# Utilities.append(boulwareUtilities(rv,Deadline))
				new_probability = probabilities
				lstmUtilities=[]

				x=[]
				for i in xrange(1,Deadline+1):
					x.append(i)
				x_belief=[]
				for i in xrange(0,Deadline+1):
					x_belief.append(i)

				GridSize=20
				Gridcoords=[GridSize/2 ,GridSize/2]

			####------ Negotiation starts ------######
				for roundnum in xrange(1,Deadline+1):


					new_CombinedUtility=0
					for i in xrange(0,len(new_probability[0])):
						new_CombinedUtility+=new_probability[roundnum-1][i]*Utilities[i][len(Utilities[i])-roundnum]

					lstmUtilities.append(float("{0:.4f}".format(new_CombinedUtility)))
					# actual_utility.append(float("{0:.4f}".format(utility_RV[len(utility_RV)-roundnum])))

			# print lstmUtilities

			##### --------- aVerages over iterations ---#####
				if(iterations==1):
					Average_rv=RV
					# AverageUtilities_Tims=actual_utility
					AverageUtilities_lstm=lstmUtilities

				else:
					Average_rv=np.array(Average_rv,dtype=float)*(iterations-1)
					# AverageUtilities_Tims=np.array(AverageUtilities_Tims,dtype=float)*(iterations-1)
					AverageUtilities_lstm=np.array(AverageUtilities_lstm,dtype=float)*(iterations-1)

					# print Average_rv
					Average_rv=map(operator.add,Average_rv,RV)
					# AverageUtilities_Tims=map(operator.add,AverageUtilities_Tims,actual_utility)
					AverageUtilities_lstm=map(operator.add,AverageUtilities_lstm,lstmUtilities)

					Average_rv=np.array(Average_rv)/iterations
					# AverageUtilities_Tims=np.array(AverageUtilities_Tims)/iterations
					AverageUtilities_lstm=np.array(AverageUtilities_lstm)/iterations

				### Commented by Kritika
				# print "---- " + str(iterations) + " -----"
				###

			
			lstmError=0

			for i in xrange(2,6):
				lstm_fit=np.polyfit(x,AverageUtilities_lstm,i,full=True)

				if(i==2):
					
					lstmError=lstm_fit[1]

					lstm_index=i

				else:
					
					if(lstm_fit[1]<lstmError):
						lstmError=lstm_fit[1]
						lstm_index=i


			legend_properties = {'weight':'bold', 'size':20}			
			

			plt.figure('AverageUtilities lstm')
			plt.title('LSTM',fontsize=20, fontweight='bold')
			coefs=poly.polyfit(x,AverageUtilities_lstm,lstm_index)
			ffit=poly.polyval(x,coefs)

			
			Bay,=plt.plot(x,AverageUtilities_lstm, linestyle='-', color='k', linewidth=1.5)
			Bayfit,=plt.plot(x,ffit, linestyle='--', color='g', linewidth=3.5)
			plt.legend([Bay,Bayfit],["LSTM Utilities","Fitted Utilities"],loc=6,ncol=1, handlelength=4,prop=legend_properties)

			plt.yticks(fontsize=20,fontweight='bold')
			plt.xticks(fontsize=20,fontweight='bold')
			# plt.plot(Average_rv,'ro')
			# plt.plot(AverageUtilities_Normalised,'r--',ffit,'g--')
			plt.xlabel('Rounds',fontsize=20, fontweight='bold')
			plt.ylabel('Utilities',fontsize=20, fontweight='bold')
			plt.savefig('lstm.pdf',format='pdf', dpi=1000)

			### Commented by Kritika
			# print '######################'
			# print "Smoothness"
			###
			print lstmError

			### Commented by Kritika
			# print '######################'
			###