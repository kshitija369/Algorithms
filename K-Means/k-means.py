#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 14:59:06 2017

@author: kshitijap
"""

import sys
import random

datafile = sys.argv[1]
labelfile = sys.argv[2]
cls_count = int(sys.argv[3])

#datafile = "/Users/kshitijap/Desktop/Summer17/ML_Assignments/Assignment6/input1"
#labelfile = "/Users/kshitijap/Desktop/Summer17/ML_Assignments/Assignment6/output1"
#cls_count = 3

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
  
f = open(labelfile, "w")       
labels = {}

#### Assign initial values to the clusters ####
#### 1 way to do that : Calculate mean of all samples and add random values to initialize all clusters
#####Compute mean#####
m = []
for i in range(0, cols, 1):
   m.append(0)
   
for i in range(0, rows, 1):
    for j in range(0, cols, 1):
        m[j] = m[j] + data[i][j]

for j in range(0, cols, 1):
    m[j] = m[j]/rows    
     

#### Assign cluster values #####
k = {}
for i in range(0,cls_count,1):
    s = []
    for j in range(0,cols,1):
       s.append(((random.random() * m[j]) * ((-1)**i)) + m[j] )
    k[i] = s  

#### Stopping condition parameters ####
dell = 0.1
err = 0
prev_err = 0
count = 0

while(True):
    prev_err = err
    err = 0
    d = []
    n = []
    
    for j in range(0,cls_count,1):
        n.append(1)
        d.append(0)
    
    for i in range(0, rows, 1):
        for x in range(0,cls_count,1):
            for j in range(0, cols, 1):
                # Calculate dist from cluster x
                d[x] = d[x] + abs(data[i][j] - k[x][j])
                    
        # Assign sample to cluster with minimum dist        
        cluster = d.index(min(d))  
        labels[i] = cluster
        n[cluster] += 1       
    
    #### Compute objective - Summation of Dist from the mean for all clusters ####
    for x in range(0,cls_count,1):
        for i in range(0,rows,1):
            for j in range(0,cols,1):
                err = err + (data[i][j] - k[x][j])**2
                            
    count += 1
    ### Check for convergence ### 
    if(abs(prev_err - err) < dell):
        break;
    if(count > 10):
        break;
    
    ### Recompute the cluster ###
    for x in range(0,cls_count,1):    
        if(n[x] > 0):
            m = []
            for i in range(0, cols, 1):
               m.append(0)
            
            for i in range(0, rows, 1):
                if(labels.get(i) != None and labels[i] == x):
                    for j in range(0, cols, 1):
                        m[j] = m[j] + data[i][j]            
                   
            for j in range(0, cols, 1):
                m[j] = m[j]/n[x]    
            k[x] = m 
    
#### Write final labels  ####
print("Final k values")
for x in range(0, cls_count, 1):
    print(k[x])
print("--------------------------\n") 
print("Predicted Labels")    
for i in range(0, rows, 1):
    print("{0} {1}\n".format(labels[i], i))
    f.write(str("{0} {1}\n".format(labels[i], i)))   
f.close()
            
     