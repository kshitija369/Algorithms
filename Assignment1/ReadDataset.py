#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 19:53:53 2017

@author: kshitijap
"""
import sys, getopt
import os
import logging
import pandas

def main(argv):
   
   path = ''
   loglevel = ''
   
   rootLogger = logging.getLogger()
   logfileName = 'ReadDataset'
   consoleHandler = logging.StreamHandler()  
   rootLogger.addHandler(consoleHandler) 
   
   try:
      opts, args = getopt.getopt(argv,"hi:l:",["ifile=","log="])
   except getopt.GetoptError:
      rootLogger.info('ReadDataset.py -i <datasetDir> -l <logLevel>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         rootLogger.info('ReadDataset.py -i <datasetDir> -l <logLevel>')
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
   count = 0
    
   for dataset in listDir:
       if not dataset.startswith('.'):
           count = count + 1
           rootLogger.info("Preparing Test and Train data for : %s", dataset)
           
           #Read actual data 
           datafile = pandas.read_csv("{0}/Dataset/{1}/{1}.data".format(path, dataset), sep = ' ',  header=None)
           
           #Read true labels
           labelsfile = pandas.read_csv("{0}/Dataset/{1}/{1}.labels".format(path, dataset), sep = ' ',  header=None)
            
           for i in range(10):
               #Read train labels 
               trainlabels = labelsfile = pandas.read_csv("{0}/Dataset/{1}/{1}.trainlabels.{2}".format(path, dataset, i), sep = ' ',  header=None)
               
           

#function to merge train labels and actual data
def mergeXnDF(y_labels, rownum):
    return(0)
    
    
if __name__ == "__main__":
   main(sys.argv[1:])
   
    

