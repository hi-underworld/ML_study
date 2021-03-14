#!/usr/bin/env python
# coding=utf-8
import numpy as np
import random
def sign(x):
    if x <= 0:
        return 0
    else:
        return 1

train = np.loadtxt(open("train.csv","rb"),delimiter=",",skiprows=0)
test = np.loadtxt(open("test.csv","rb"),delimiter=",",skiprows=0)
weights = np.zeros(784)
bias = 0
times = 200000
rate = 1
#training process,
#training data include 0-39999 in 'train')
while times > 0:
    i = random.randint(0,39999)
    parameters = np.resize(train[i][1:], (784,1))
    real_output = sign(weights.dot(parameters) + bias)
    actual_label = train[i][0]
    if real_output != actual_label:
        weights = weights + rate * (actual_label - 0.5)* train[i][1:]
        bias =  bias + rate * (actual_label - 0.5)
        #print(bias)
    times -= 1

#computing the accuracy, precison and recall ratio; testing data includes 40000-41999 in 'train')
#Here, define the 'label = 0' as negative class, 'label = 1' as positive class
TP = 0
FP = 0
TN = 0
FN = 0
for j in range(40000,42000):
    parameters = np.resize(train[j][1:], (784,1))
    real_output = sign(weights.dot(parameters) + bias)
    actual_label = train[j][0]
    if actual_label == 0:
        if real_output != actual_label:
            FP += 1
        else:
            TN += 1
    else:
        if real_output != actual_label:
            FN += 1
        else:
            TP += 1
print('TP is %d' % TP)
print('FP is %d' % FP)
print('TN is %d' % TN)
print('FN is %d' % FN)
print('accuracy is %f' %((TP + TN) / 2000.0))
print('precision is %f' %(TP / (TP + FP)))
print('recall is %f' %(TP / (TP + FN)))

#test process
predict_labels = []
for k in range(28000):
    parameters = np.resize(test[k], (784,1))
    predict_output = sign(weights.dot(parameters) + bias)
    predict_labels.append(predict_output)
print(predict_labels)
    
