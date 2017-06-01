#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 31 17:54:23 2017

@author: kshitijap
"""
import sys, getopt
import os
import logging
import pandas

rootLogger = None

def main(argv):
   
   global rootLogger
   path = ''
   loglevel = ''
   
   rootLogger = logging.getLogger()
   logfileName = 'BalancedError'
   consoleHandler = logging.StreamHandler()  
   rootLogger.addHandler(consoleHandler)   
   try:
      opts, args = getopt.getopt(argv,"hi:l:",["ifile=","log="])
   except getopt.GetoptError:
      rootLogger.info('BalancedError.py -i <datasetDir> -l <logLevel>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         rootLogger.info('BalancedError.py -i <datasetDir> -l <logLevel>')
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
           error = 0
           for i in range(10):
               #Read test data
               testdata = pandas.read_csv("{0}/Dataset/{1}/{1}.testdata.{2}.csv".format(path, dataset, i), sep = ',',  header=None, index_col=False)              
               lastcolidx = len(testdata.columns) - 1
               testlabels = list(testdata.loc[:, lastcolidx]) 
               
               #Read prediction data
               preddata = pandas.read_csv("{0}/Dataset/{1}/{1}.preddata.{2}.csv".format(path, dataset, i), sep = ',',  header=None, index_col=False) 
               preddata = list(preddata[1])
               a=b=c=d=0
               
               for i in range(len(preddata)):
                   if(preddata[i] == 0 & testlabels[i] == 0): 
                       a=a+1 
                   if(preddata[i] == 0 & testlabels[i] == 1): 
                       b=b+1 
                   if(preddata[i] == 1 & testlabels[i] == 0): 
                       c=c+1 
                   if(preddata[i] == 1 & testlabels[i] == 1): 
                       d=d+1 
               error = error + 0.5*(b/(a+b) + c/(c+d))       
               
           error = error/10               
           rootLogger.info("Balanced error for dataset %s : %0.2f", dataset, error)
               
if __name__ == "__main__":
   main(sys.argv[1:])               
               