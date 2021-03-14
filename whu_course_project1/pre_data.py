#!/usr/bin/env python
# coding=utf-8
def str2int(str)
    train_data =[]
    with open(str , 'r') as train:
        for line in train:
            line_list = list(line)
            if line_list[0] == '0' || line_list[0] == '1':
                train_data.append(line_list)
    return train_data
