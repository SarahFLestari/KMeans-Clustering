import matplotlib.pyplot as pyplot
import numpy as nmp
import math
from collections import Counter

dataTrain = []
x = []
y = []
arr = []

file = open('TrainsetTugas2.txt')

#read data 
with open('TrainsetTugas2.txt') as f:
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
centroid = []
centroid = nmp.random.rand(k,2)

# print(centroid)

for i in range(len(dataTrain)):
	for j in range(len(centroid)):
		jarak = []
		hasil = euclid(dataTrain[i][0],dataTrain[i][1],centroid[j][0],centroid[j][1])
		jarak.append(hasil)
		print(count(jarak))

	





