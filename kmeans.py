import matplotlib.pyplot as pyplot
import numpy as nmp
import math
from collections import Counter

dataTrain = []
x = []
y = []
arr = []

# file = open('TrainsetTugas2.txt')

# #read data 
# with open('TrainsetTugas2.txt') as f:
# 	lines = f.readlines()
# 	x = [float(line.split()[0]) for line in lines]
# 	y = [float(line.split()[1]) for line in lines]

file = open('train.txt')

#read data 
with open('train.txt') as f:
	lines = f.readlines()
	x = [float(line.split()[0]) for line in lines]
	y = [float(line.split()[1]) for line in lines]

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

k = 3
centroid = [[nmp.random.uniform(0,40),nmp.random.uniform(0,35)] for i in range(k)]

# print("ini centroid")
# print(centroid)

dist = []
cent = 0
for i in range(len(centroid)):
	dist.append([])
	for j in range(len(dataTrain)):
		hasil = euclid(dataTrain[j][0],dataTrain[j][1],centroid[i][0],centroid[i][1])
		dist[cent].append(hasil)
	cent+=1
print("ini distance")
print(dist)
kelas = nmp.array(dist)
datakelas = []
allAvg = []
for i in range(len(kelas[0])):
	kolom = kelas[:,i]
	print (kolom.tolist().index(min(kolom)))
	datakelas.append([kolom.tolist().index(min(kolom))+1, min(kolom)])
print(datakelas)
dataCluster = []
count = 0
for s in range(k):
	dataCluster.append([])
	for g in range(len(datakelas)):
		if (datakelas[g][0] == s+1):
			dataCluster[count].append(datakelas[g][1])
	allAvg.append(sum(dataCluster[count])/)	
	count+=1
print(dataCluster)
print(allAvg)
# datakelas1 = []
# datakelas2 = []
# datakelas3 = []


# for j in range(len(datakelas)):
# 	if (datakelas[j][0] == 0):
# 		datakelas1.append(datakelas[j][1])
# 		datakelas[j][0] = 1
# 		# print(datakelas[j][1])
# 	elif (datakelas[j][0] == 1):
# 		datakelas2.append(datakelas[j][1])
# 		datakelas[j][0] = 2
# 		# print(datakelas[j][1])
# 	elif (datakelas[j][0] == 2):
# 		datakelas3.append(datakelas[j][1])
# 		datakelas[j][0] = 3
# 		# print(datakelas[j][1])
# print(datakelas)
# print("jumlah kelas 1",sum(datakelas1))
# print("jumlah kelas 2",sum(datakelas2))
# print("jumlah kelas 3",sum(datakelas3))



# for z range(len(centroid)):

		

	





