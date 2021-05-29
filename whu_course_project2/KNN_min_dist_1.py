import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

train = np.loadtxt(open("mnist_train.csv","rb"),delimiter=",",skiprows=0)
test = np.loadtxt(open("mnist_test.csv","rb"),delimiter=",",skiprows=0)

for i in range(60000):
    if train[i][0] != 0:
        train[i][0] = 1

x_train = train[:,1:]
y_train = train[:,0]

for i in range(10000):
    if test[i][0] != 0:
        test[i][0] = 1

x_test = test[:,1:]
y_test  = test[:,0]

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

result = knn.predict(x_test, y_test)
for i in range(10000):
    if result[i] == 1:
        count = count + 1

print('the accuracy is %f' %(count / 10000))
