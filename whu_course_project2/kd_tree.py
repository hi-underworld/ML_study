import numpy as np
from functools import cmp_to_key

def create_kd_tree(data, depth, k, father):
    length = len(data)
    data_copy = data[:]
    dimension = depth % k + 1
    data_copy = sorted(data_copy, key = cmp_to_key(lambda x, y: x[dimension] - y[dimension]))
    data_copy = np.asarray(data_copy)
    depth += 1
    if length == 0:
        #print('fail to create')
        return None
    elif length == 1:
        return {'node':data[0], 'depth': depth, 'dimension': dimension, 'left': None , 'right': None, 'father' : father}
    elif length > 1:
        mid = length // 2
        print(mid)
        data_left = data_copy[:mid, :]
        data_right = data_copy[(mid + 1):, :]
        left_tree = create_kd_tree(data_left)
        right_tree = create_kd_tree(data_right)
        left_tree['father'] = right_tree['father'] = {'node': data[mid], 'depth': depth, 'dimension': dimension, 'left': left_tree, 'right': right_tree, 'father': father}
        return {'node': data[mid], 'depth': depth, 'dimension': dimension, 'left': left_tree, 'right': right_tree, 'father': father}

def distance(target, source):
    length = len(target)
    dist = 0
    for i in range(1, length):
        dist += (target[i] - source[i]) ** 2
    dist = dist ** 0.5
    return dist

def search_point(kd_tree, target):
    current_closest =[]
    if kd_tree['left'] != None | kd_tree['right'] != None:
        dimension = kd_tree['dimension']
        if target[dimension] > (kd_tree['node'])[dimension]:
            search_point(kd_tree['right'], target)
        elif target[dimension] <= (kd_tree['node'])[dimension]:
            search_point(kd_tree['left'], target)
    elif kd_tree['left'] == None & kd_tree['right'] == None:
        current_closest = kd_tree
        return current_closest

def back_tree(kd_tree, target)
    if(kd_tree['father'] != None):
        if distance(((kd_tree['father'])['right'])['node'], target) >= distance(kd_tree, target):
            back_tree(kd_tree['father'], target)
        elif distance(((kd_tree['father'])['right'])['node'], target) < distance(kd_tree, target):
            kd_tree = (kd_tree['father'])['right']
            back_tree(kd_tree['father'], target)
    elif(kd_tree['father'] == None):
        return kd_tree

train = np.loadtxt(open("train.csv","rb"),delimiter=",",skiprows=0)
train_data = train[:39999,:]
test_data = train[40000:41999,:]

KD_tree = create_kd_tree(train, 0, 784)
errors = 0
for i in range(2000):
    current_closest = search_point(KD_tree, test_data[i])
    final_closest= back_tree(current_tree, test_data[i])
    if final_closest['node'][0] != test_data[i][0]:
        error += 1
accuracy = errors / 2000
print (accuracy)