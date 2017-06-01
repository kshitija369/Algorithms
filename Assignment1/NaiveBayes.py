#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 14:25:36 2017

@author: kshitijap
"""
import sys, getopt, csv
import os
import logging
import pandas

rootLogger = None

def main(argv):
   
   global rootLogger
   path = ''
   loglevel = ''
   
   rootLogger = logging.getLogger()
   logfileName = 'NaiveBayes'
   consoleHandler = logging.StreamHandler()  
   rootLogger.addHandler(consoleHandler)   
   try:
      opts, args = getopt.getopt(argv,"hi:l:",["ifile=","log="])
   except getopt.GetoptError:
      rootLogger.info('NaiveBayes.py -i <datasetDir> -l <logLevel>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         rootLogger.info('NaiveBayes.py -i <datasetDir> -l <logLevel>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         path = arg
         logPath = path
      elif opt in ("-l", "--log"):
         loglevel = arg
         
    
   fileHandler = logging.FileHandler("{0}/{1}.log".format(logPath, logfileName))
   rootLogger.addHandler(fileHandler)
   # set user specified log level
   numeric_level = getattr(logging, loglevel.upper(), None)
   if not isinstance(numeric_level, int):
       raise ValueError('Invalid log level: %s' % loglevel)
   rootLogger.setLevel(numeric_level)
   # set working dir as folder with datasets
   os.chdir(path)
    
   # list all the files in the dataset folder
   listDir = os.listdir("{0}/Dataset/".format(path))
    
   for dataset in listDir:
       if not dataset.startswith('.'):
           rootLogger.info("Working with dataset : %s", dataset)
           for i in range(10):
               #Read train data
               datafile = pandas.read_csv("{0}/Dataset/{1}/{1}.traindata.{2}.csv".format(path, dataset, i), sep = ',',  header=None, index_col=False)
               #Read test data
               testdata = pandas.read_csv("{0}/Dataset/{1}/{1}.testdata.{2}.csv".format(path, dataset, i), sep = ',',  header=None, index_col=False)              
               lastcolidx = len(datafile.columns) - 1
               testfile = testdata.loc[:, 0:(lastcolidx-1)] 
               uq_classes = list(set(datafile.loc[:,lastcolidx]))
               dict_mean = {}
               dict_std = {}
               pred = {}
               m = []
               s = []
               loss = []
               
               for class_ in uq_classes:
                   class_data = datafile.loc[datafile[lastcolidx] == class_, 0:(lastcolidx - 1)]
                   m = [1]*(lastcolidx - 1)   #List of mean of every column except the label
                   s = [1]*(lastcolidx - 1)   #List of std of every column except the label
                   m = list(class_data[:].mean())
                   s = list(class_data[:].std())
                   dict_mean[class_] = m
                   dict_std[class_] = s         
                      
               #Predictions
               for index, row in testfile.iterrows():
                   loss = []
                   for class_ in uq_classes:
                       lossvalue = 0
                       m = dict_mean[class_]
                       s = dict_std[class_]
                       lossvalue = sum(((row - m)/s)**2)
                       loss.append(lossvalue)   
                   pred[index] = loss.index(min(loss))
                   
               with open("{0}/Dataset/{1}/{1}.preddata.{2}.csv".format(path, dataset, i), 'w') as csv_file:
                   writer = csv.writer(csv_file, delimiter=',')
                   for key, value in pred.items():
                       writer.writerow([str(key),str(value)])   


if __name__ == "__main__":
   main(sys.argv[1:])       
