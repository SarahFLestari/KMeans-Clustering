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

# memasukkan data kedalam array

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


def kmeans(k,centroid):
	dist = []
	cent = 0
	for i in range(len(centroid)):
		dist.append([])
		for j in range(len(dataTrain)):
			hasil = euclid(dataTrain[j][0],dataTrain[j][1],centroid[i][0],centroid[i][1])
			dist[cent].append(hasil)
		cent+=1
	kelas = nmp.array(dist)
	datakelas = []
	for i in range(len(kelas[0])):
		kolom = kelas[:,i]
		#print (kolom.tolist().index(min(kolom)))
		datakelas.append([kolom.tolist().index(min(kolom))+1, dataTrain[i]])
	dataClustery = []
	count = 0
	jmldatapercluster = []
	clstr = []
	sum_kelas=[]
	centroidBaru = []
	# for i in datakelas:
	# 	for j in k:

	for j in range(k):
		dataClusterx = 0
		jum_x = 0
		dataClustery = 0
		jum_y = 0
		for i in datakelas:
			if i[0] == j+1:
				dataClusterx += i[1][0]
				jum_x +=1
				dataClustery += i[1][1]
				jum_y +=1
		centroidBaru.append([dataClusterx/jum_x,dataClustery/jum_y]	)
	print("baru",centroidBaru)
	return (centroidBaru)

k = 7
centroid = [[nmp.random.uniform(0,40),nmp.random.uniform(0,35)] for i in range(k)]
centroidLama = [0,0]
iterasi = 0

while True:
	centroidLama = centroid
	centroid = kmeans(k,centroid)
	iterasi+=1
	print(iterasi, centroid)
	if centroidLama == centroid:
		for k in range(len(centroid)):
			pyplot.scatter(centroid[k][0],centroid[k][1],marker='D', alpha=1)
		break
for i in range(len(dataTrain)):
 	pyplot.scatter(dataTrain[i][0], dataTrain[i][1],color='r', alpha=0.5)

pyplot.title('Visualisasi data training')
pyplot.show()




# Centroid terbaik	
# [[33.10967741935484, 8.782258064516133], [32.65272727272726, 22.114545454545446], [9.017266187050357, 22.982374100719433], [19.39664634146342, 6.800304878048779], [21.47124999999999, 23.16875], [9.44473684210526, 4.123684210526316], [11.273529411764706, 10.991176470588242]]


	
# 9 [[21.623076923076916, 23.02820512820513], [33.10967741935484, 8.782258064516133]
# , [32.65272727272726, 22.114545454545446], [6.53, 3.5116666666666663], 
# [9.094366197183097, 25.742253521126763], [9.39407894736842, 19.92302631578947], 
# [8.683333333333335, 11.028888888888886], [21.372619047619047, 6.154166666666666], 
# [17.06136363636363, 10.126515151515154], [14.580405405405406, 5.120945945945947]]

# [[33.10833333333334, 8.586111111111116], [18.563698630136997, 4.223972602739728], 
# [13.847191011235953, 8.076966292134832], [7.385483870967742, 11.782258064516125], 
# [20.96554054054054, 8.927027027027027], [9.04, 25.58], [32.55200000000001, 25.058000000000003],
#  [9.467361111111112, 19.76875], [32.7563492063492, 19.423809523809524], [6.843749999999999, 3.5265625], 
#  [21.623076923076916, 23.02820512820513]]

# [[8.054054054054056, 11.525675675675673], [9.094366197183097, 25.742253521126763], [14.022159090909092, 6.21875], [20.925657894736837, 5.233552631578946], [32.55200000000001, 25.058000000000003], [32.7563492063492, 19.423809523809524], [9.39407894736842, 19.92302631578947], [18.65808823529412, 10.133823529411764], [21.623076923076916, 23.02820512820513], [33.10833333333334, 8.586111111111116], [6.53, 3.5116666666666663]]
# [[6.4684210526315775, 22.993859649122808], [32.55454545454546, 24.79181818181818], [7.29861111111111, 3.7708333333333335], [14.643749999999994, 9.201874999999998], [16.789130434782614, 4.223188405797103], [7.574242424242426, 11.633333333333331], [32.77155172413793, 19.190517241379315], [21.623076923076916, 23.02820512820513], [33.10833333333334, 8.586111111111116], [11.163750000000004, 26.603749999999998], [21.53456790123457, 7.638271604938271], [10.888, 19.340999999999998]]
