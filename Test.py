import matplotlib.pyplot as pyplot
import numpy as nmp
import math
from collections import Counter

dataTest= []
file = open('TestsetTugas2.txt')


#read data 
with open('TestsetTugas2.txt') as f:
	lines = f.readlines()
	x = [float(line.split()[0]) for line in lines]
	y = [float(line.split()[1]) for line in lines]
for i in range(len(y)) :
	dataTest.append([x[i],y[i]])
def euclid (x1,y1,x2,y2):
    hasil = math.sqrt((math.pow(x2-x1,2))+(math.pow(y2-y1,2)))
    return hasil

# centroid = [[6.4684210526315775, 22.993859649122808], [32.55454545454546, 24.79181818181818], [7.29861111111111, 3.7708333333333335], [14.643749999999994, 9.201874999999998], [16.789130434782614, 4.223188405797103], [7.574242424242426, 11.633333333333331], [32.77155172413793, 19.190517241379315], [21.623076923076916, 23.02820512820513], [33.10833333333334, 8.586111111111116], [11.163750000000004, 26.603749999999998], [21.53456790123457, 7.638271604938271], [10.888, 19.340999999999998]]
centroid = [[33.10967741935484, 8.782258064516133], [32.65272727272726, 22.114545454545446], [9.017266187050357, 22.982374100719433], [19.39664634146342, 6.800304878048779], [21.47124999999999, 23.16875], [9.44473684210526, 4.123684210526316], [11.273529411764706, 10.991176470588242]]

dist = []
cent = 0
for i in range(len(centroid)):
	dist.append([])
	for j in range(len(dataTest)):
		hasil = euclid(dataTest[j][0],dataTest[j][1],centroid[i][0],centroid[i][1])
		dist[cent].append(hasil)
	cent+=1
kelas = nmp.array(dist)
datakelas = []
for i in range(len(kelas[0])):
	kolom = kelas[:,i]
	#print (kolom.tolist().index(min(kolom)))
	datakelas.append([kolom.tolist().index(min(kolom))+1, dataTest[i]])
print(datakelas)



clstr1 = []
clstr2 = []
clstr3 = []
clstr4 = []
clstr5 = []
clstr6 = []
clstr7 = []

for i in range(len(datakelas)):
	if(datakelas[i][0] == 1):
		clstr1.append(datakelas[i])
	elif(datakelas[i][0] == 2):
		clstr2.append(datakelas[i])
	elif(datakelas[i][0] == 3):
		clstr3.append(datakelas[i])
	elif(datakelas[i][0] == 4):
		clstr4.append(datakelas[i])	
	elif(datakelas[i][0] == 5):
		clstr5.append(datakelas[i])	
	elif(datakelas[i][0] == 6):
		clstr6.append(datakelas[i])	
	elif(datakelas[i][0] == 7):
		clstr7.append(datakelas[i])	
print(len(clstr1))
print(len(clstr2))
print(len(clstr3))
print(len(clstr4))
print(len(clstr5))
print(len(clstr6))
print(len(clstr7))
# print(clstr1)
# print(clstr2)
# print(clstr3)
# print(clstr4)
for i in range(len(clstr1)):
	pyplot.scatter(clstr1[i][1][0],clstr1[i][1][1],color='b')
for i in range(len(clstr2)):
	pyplot.scatter(clstr2[i][1][0],clstr2[i][1][1],color='g')
for i in range(len(clstr3)):
	pyplot.scatter(clstr3[i][1][0],clstr3[i][1][1],color='r')
for i in range(len(clstr4)):
	pyplot.scatter(clstr4[i][1][0],clstr4[i][1][1],color='y')
for i in range(len(clstr5)):
	pyplot.scatter(clstr5[i][1][0],clstr5[i][1][1],color='w')
for i in range(len(clstr6)):
	pyplot.scatter(clstr6[i][1][0],clstr6[i][1][1],color='cyan')
for i in range(len(clstr7)):
	pyplot.scatter(clstr7[i][1][0],clstr7[i][1][1],color='m')
for i in range(len(centroid)):
	pyplot.scatter(centroid[i][0],centroid[i][1],color='k')
	
file = open("prediksi.txt","w")
for m in range(len(datakelas)):
    file.write(str(datakelas[m]))
    file.write("\n")

file.close()
pyplot.title('Visualisasi data test')
pyplot.show()	