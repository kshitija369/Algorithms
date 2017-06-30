#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 16:29:50 2017

@author: kshitijap
"""

import sys
import random

datafile = sys.argv[1]
labelfile = sys.argv[2]

#datafile = "/Users/kshitijap/Desktop/Summer17/ML_Assignments/Assignment2/input"
#labelfile = "/Users/kshitijap/Desktop/Summer17/ML_Assignments/Assignment2/output"


f = open(datafile)
data = []
i = 0
l = f.readline()

#####Read Data######
while(l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
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
    trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1
f.close()

w = []
#####Initialize w #####
for j in range(0, cols, 1):
    w.append(.02 * random.random() - .01)
    
#####Gradiant descend constants #####
eta = .001
stop =  .0001

##### Function dot product #####
def dot_product(w_, data_i ):
    dp = 0
    for j in range(0, cols, 1):
        dp += w_[j] * data_i[j]
    return(dp);

old_w = []
for j in range(0, cols, 1):
    old_w.append(0)
while True:
    ##### Find dellf #####
    dellf = []
    flag = False
    for j in range(0, cols, 1):
        dellf.append(0)
    
    for i in range(0, rows, 1):
         y = dot_product(w,data[i])
         for j in range(0, cols, 1):
             dellf[j] += (trainlabels[i] - y) * data[i][j]
    
    ##### Update w #####
    for j in range(0, cols, 1):
        old_w[j] =  w[j]
        w[j] = w[j] + eta * dellf[j]
        
    # Check for convergence
    for k in range(0, cols, 1):
        if(abs(old_w[k] - w[k]) <= stop):
            flag = True
    if(flag == True):
        break;    
        
    ##### Calculate Error #####
    error = 0
    for i in range(0, rows, 1):
        error += (trainlabels[i] - dot_product(w,data[i]))**2
    
    print("error : ", error)

print("w : ")
normw = 0
for j in range(0, cols, 1):
    normw += w[j]**2 
    print(w[j])
    
print("\n")
normw = (normw)**0.5
print("||w|| : ", normw)
print("abs(w0/||w||) :", abs(w[0]/normw))





