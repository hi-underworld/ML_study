import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

points = [[1.5,5,0],[2.5,4.7,0],[3,2.5,0],[2.8,1,0],[4.5,4.2,0],[6,2,0],[8,2,0],[1,3,1],[2,8,1],[3,7,1],[4,6,1],[5,6.2,1],[5,3.2,1],[7.2,3.5,1],[8,4,1],[7.2,7,1],[5,8,1],[9,7.5,1]]
points_x = []
points_y = []

for i in range(18):
    points_x.append([points[i][0], points[i][1]])
    points_y.append(points[i][2])
    if i <= 6:
        plt.plot(points[i][0], points[i][1], 'ko')
    elif i >= 7:
        plt.plot(points[i][0], points[i][1], 'k*')

plt.axis([0,10,0,10])

knn = KNeighborsClassifier(2)
knn.fit(points_x, points_y)

for i in range(200):
    x = 0.05 * i
    for j in range(200):
        y = 0.05 * j
        if knn.predict([[x,y]]) == 0:
            plt.plot(x,y, c = 'blue', marker = ',', markersize = 20)
        elif knn.predict([[x,y]]) == 1:
            plt.plot(x, y, c = 'darkred', marker = ',',markersize = 20)

plt.show()