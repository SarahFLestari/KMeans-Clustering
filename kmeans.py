import matplotlib.pyplot as pyplot
import numpy as nmp
import math
from collections import Counter

dataTrain = []
x = []
y = []

file = open('TrainsetTugas2.txt')

#read data 
with open('TrainsetTugas2.txt') as f:
	lines = f.readlines()
	x = [float(line.split()[0]) for line in lines]
	y = [float(line.split()[1]) for line in lines]

# file = open('train.txt')

# #read data 
# with open('train.txt') as f:
# 	lines = f.readlines()
# 	x = [float(line.split()[0]) for line in lines]
# 	y = [float(line.split()[1]) for line in lines]

#memasukkan data kedalam array

for i in range(len(y)) :
	dataTrain.append([x[i],y[i]])

# print(dataTrain)

# rumus euclidean
def euclid (x1,y1,x2,y2):
    hasil = math.sqrt((math.pow(x2-x1,2))+(math.pow(y2-y1,2)))
    return hasil

 # visualisasi
for i in range(len(dataTrain)):
 	pyplot.scatter(dataTrain[i][0], dataTrain[i][1], color='r')

# pyplot.title('Visualisasi data training')
# pyplot.show()
k = 4
centroidC = [[nmp.random.uniform(0,40),nmp.random.uniform(0,35)] for i in range(k)]
print(centroidC)
centroid= []

while (centroidC != centroid):
	for m in range(10):
		centroid = centroidC
		dist = []
		cent = 0
		for i in range(len(centroid)):
			dist.append([])
			for j in range(len(dataTrain)):
				hasil = euclid(dataTrain[j][0],dataTrain[j][1],centroid[i][0],centroid[i][1])
				dist[cent].append(hasil)
			cent+=1
		# print("ini distance")
		# print(dist)
		kelas = nmp.array(dist)
		datakelas = []
		avgx = []
		avgy = []
		avg = []
		for i in range(len(kelas[0])):
			kolom = kelas[:,i]
			#print (kolom.tolist().index(min(kolom)))
			datakelas.append([kolom.tolist().index(min(kolom))+1, dataTrain[i]])
		print(datakelas)

		dataClusterx = []
		dataClustery = []
		count = 0
		jmldatapercluster = []
		for s in range(k):
			dataClusterx.append([])
			dataClustery.append([])
			for g in range(len(datakelas)):
				if (datakelas[g][0] == s+1):
					dataClusterx[count].append(datakelas[g][1][0])
					dataClustery[count].append(datakelas[g][1][1])
			if (len(dataClusterx[count]) != 0):
				avg.append([sum(dataClusterx[count])/len(dataClusterx[count]),sum(dataClustery[count])/len(dataClustery[count])])
			else :
				avg.append([0,0])
			count+=1
		print(avg)
		centoird = avg
		print(centroid)


clstr1 = []
clstr2 = []
clstr3 = []
clstr4 = []
for i in range(len(datakelas)):
	if(datakelas[i][0] == 1):
		clstr1.append(datakelas[i])
	elif(datakelas[i][0] == 2):
		clstr2.append(datakelas[i])
	elif(datakelas[i][0] == 3):
		clstr3.append(datakelas[i])
	elif(datakelas[i][0] == 4):
		clstr4.append(datakelas[i])	
print(clstr1)
print(clstr2)
print(clstr3)
print(clstr4)
for i in range(len(clstr1)):
	pyplot.scatter(clstr1[i][1][0],clstr1[i][1][1],color='r')
for i in range(len(clstr2)):
	pyplot.scatter(clstr2[i][1][0],clstr2[i][1][1],color='g')
for i in range(len(clstr3)):
	pyplot.scatter(clstr3[i][1][0],clstr3[i][1][1],color='b')
for i in range(len(clstr4)):
	pyplot.scatter(clstr4[i][1][0],clstr4[i][1][1],color='c')
pyplot.title('Visualisasi data training')
pyplot.show()	




		

	





