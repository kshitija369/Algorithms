#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:29:50 2017

@author: kshitijap
"""

import sys

datafile = sys.argv[1]
labelfile = sys.argv[2]

#datafile = "/Users/kshitijap/Desktop/Summer17/ML_Assignments/Assignment5/input"
#labelfile = "/Users/kshitijap/Desktop/Summer17/ML_Assignments/Assignment5/output"

f = open(datafile)
data = []
i = 0
l = f.readline()

min_col_val = {};
max_col_val = {};
             
#####Read Data######
while(l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
        #Used to determine the best split
        if(min_col_val.get(j) == None or  min_col_val.get(j) > float(a[j])):
            min_col_val[j] = float(a[j])
        if(max_col_val.get(j) == None or  max_col_val.get(j) < float(a[j])):
            max_col_val[j] = float(a[j])
            
    data.append(l2)
    l = f.readline()
    
rows = len(data)
cols = len(data[0])
f.close()

#####Read labels#####
f = open(labelfile)
trainlabels = {}
n = []
n.append(0)
n.append(0)
l = f.readline()

while(l != ''):
    a = l.split()
    # transform label class from (0,1) to (-1,1)
    if(int(a[0]) == 0):
        a[0] = -1    
    trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1
f.close()

gini = {}

for j in range(0, cols, 1):
    left_split = {}
    right_split = {}
    lp = 0
    rp = 0
    lsize = 0
    rsize = 0
    
    # Splitting the data of j th column
    split_val = (min_col_val.get(j) + max_col_val.get(j))/2
    for i in range(0, rows, 1):
        if(data[i][j] < split_val):
            left_split[i] = trainlabels[i]
        else:
            right_split[i] = trainlabels[i]
    
    #Calculating gini for the split
    lsize = len(left_split)
    rsize = len(right_split)
    
    #Calculating left and right proportion
    for i in range(0, rows, 1):
        if(left_split.get(i) != None and left_split.get(i) == -1):
            lp = lp+1
    if(lsize > 0):
        lp = lp/lsize
    else:
        lsize = 1
        
    for i in range(0, rows, 1):
        if(right_split.get(i) != None and right_split.get(i) == -1):
             rp = rp+1
    if(rsize > 0):         
        rp = rp/rsize   
    else:
        rsize = 1

    #Calculate the gini value for this split
    #gini = (lsize/rows)*(lp/lsize)*(1 - lp/lsize) + (rsize/rows)*(rp/rsize)*(1 - rp/rsize);
    gini[j] = (lsize/rows)*(lp/lsize)*(1 - lp/lsize) + (rsize/rows)*(rp/rsize)*(1 - rp/rsize)
    print("gini value for column {0} is {1}".format(j, gini[j]))

print("Column used for split is ", min(gini, key = gini.get))
