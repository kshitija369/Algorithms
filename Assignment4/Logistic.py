#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  19 15:15:59 2017

@author: kshitijap
"""

import os, sys
import random
import math

##### Function dot product #####
def dot_product(w_, data_i ):
    dp = 0
    for j in range(0, cols, 1):
        dp += w_[j] * data_i[j]
    return(dp);
 
def sigmoid(a):
    res = 0
    res = 1/(1+math.exp(-a))
    return(res);

path = sys.argv[1]
#path = "/Users/kshitijap/Desktop/Summer17/ML_Assignments/"

# list all the files in the dataset folder
listDir = os.listdir("{0}/Dataset/".format(path))

for dataset in listDir:
    if not dataset.startswith('.'):
        print("Working with dataset : ", dataset)
        datafile = "{0}/Dataset/{1}/{1}.data".format(path, dataset)
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
        for k in range(0, 10, 1):            
            #####Read labels#####
            labelfile = "{0}/Dataset/{1}/{1}.trainlabels.{2}".format(path, dataset, k)
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
                w.append(.01 * random.random() - .01)
            
            #####Gradiant descend constants #####
            eta = .001
            stop =  .000000001
            #eta = .00000001
            #stop = .000001
                
            dellf = []
            for j in range(0, cols, 1):
                    dellf.append(0)
            
            old_dellf = []
            for j in range(0, cols, 1):
                old_dellf.append(0)        
                
            while True:
                flag = False
                for j in range(0, cols, 1):
                    old_dellf[j] = dellf[j]
                
                for j in range(0, cols, 1):
                    dellf[j] = 0
            
                normw = 0
                for j in range(0, cols-1, 1):
                    normw += w[j]**2 
                ##### Find dellf #####    
                for i in range(0, rows, 1):
                    if(trainlabels.get(i) != None):          
                        
                        o = dot_product(w,data[i])
                        y = sigmoid(o)
                        
                        for j in range(0, cols, 1):
                            dellf[j] += (trainlabels[i] - y) * data[i][j]
                
                ##### Update w #####
                for j in range(0, cols, 1):
                    w[j] = w[j] + eta * dellf[j] 
                    
                # Check for convergence
                for x in range(0, cols, 1):
                    if(abs(old_dellf[x] - dellf[x]) < stop):
                        flag = True
                    else:
                        flag = False
                if(flag == True):
                    break;  
                     
                ##### Calculate Error #####
                error = 0
                for i in range(0, rows, 1):
                    if(trainlabels.get(i) != None):    
                        error += -1 * (trainlabels[i]*math.log(sigmoid(dot_product(w,data[i]))) + (1 - trainlabels[i])*math.log(1 - sigmoid(dot_product(w,data[i]))))      
                print("error : ", error)  
            
            f.close()
            print("w : ")
            normw = 0
            for j in range(0, cols-1, 1):
                normw += w[j]**2 
                          
            for j in range(0, cols, 1):              
                print(w[j])
                
            print("\n")
            normw = math.sqrt(normw)
            print("||w|| : ", normw)
            print("abs(w0/||w||) :", abs(w[cols-1]/normw))
            
            #####Classify unlabeled points#####
            predfile = "{0}/Dataset/{1}/{1}.pred.{2}".format(path, dataset, k)
            f = open(predfile, "w")              
            for i in range(0, rows, 1):
                if( trainlabels.get(i) == None):
                    #####Write predictions#####
                    if(math.log(sigmoid(dot_product(w,data[i]))) >= 0.5):
                            f.write(str("1 {0}\n".format(i)))
                    else:
                            f.write(str("0 {0}\n".format(i))) 
                              
