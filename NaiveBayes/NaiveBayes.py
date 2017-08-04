#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  18 15:00:07 2017

@author: kshitijap
"""
import os, sys

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
            #####Compute mean#####
            m0 = []
            for i in range(0, cols, 1):
               m0.append(0)
            m1 = []
            for i in range(0, cols, 1):
               m1.append(0)     

            for i in range(0, rows, 1):
                if(trainlabels.get(i) != None and trainlabels[i] == 0):
                    for j in range(0, cols, 1):
                        m0[j] = m0[j] + data[i][j]
                if(trainlabels.get(i) != None and trainlabels[i] == 1):
                    for j in range(0, cols, 1):
                        m1[j] = m1[j] + data[i][j]             
           
            for j in range(0, cols, 1):
                m0[j] = m0[j]/n[0]
                m1[j] = m1[j]/n[1]

           #####Compute Std. Deviation#####
            s0 = []
            for i in range(0, cols, 1):
               s0.append(0)
            s1 = []
            for i in range(0, cols, 1):
               s1.append(0)     

            for i in range(0, rows, 1):
                if(trainlabels.get(i) != None and trainlabels[i] == 0):
                    for j in range(0, cols, 1):
                        s0[j] = s0[j] + (data[i][j] - m0[j])**2
                if(trainlabels.get(i) != None and trainlabels[i] == 0):
                    for j in range(0, cols, 1):
                        s1[j] = s1[j] + (data[i][j] - m1[j])**2             
           
            for j in range(0, cols, 1):
                s0[j] = (s0[j]/n[0])**0.5
                s1[j] = (s1[j]/n[1])**0.5    
           
            #####Classify unlabeled points#####
            predfile = "{0}/Dataset/{1}/{1}.pred.{2}".format(path, dataset, k)
            f = open(predfile, "w")              
            for i in range(0, rows, 1):
                if( trainlabels.get(i) == None):
                    d0 = 0
                    d1 = 0
                    for j in range(0, cols, 1):
                        if(s0[j] != 0 and s1[j] != 0):
                            d0 = d0 + ((data[i][j] - m0[j])/s0[j])**2
                            d1 = d1 + ((data[i][j] - m1[j])/s1[j])**2     
                    #####Write predictions#####
                    if( d0 < d1):              
                        f.write(str("0 {0}\n".format(i)))
                    else:
                        f.write(str("1 {0}\n".format(i)))
           

                      


