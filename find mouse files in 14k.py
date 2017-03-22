# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 17:50:17 2016

@author: Krishna
"""
import os
import time
import shutil
c=0

start_time = time.time()
for path, dirs, files in os.walk(r'E:\F DRIVE\M.Tech\for assigning cl\selected\random 500_ll'):                    
    for filee in files:
        sentences = open(os.path.join(path,filee), encoding='utf-8').readlines();
        c = c+1
        r=0
        print (c) # one value printed for each file
        print("--- %s seconds ---" % (time.time() - start_time))
        for s in sentences:
            if s.startswith('!Sample_organism_ch1\t"Mus musculus"'):
                r=1
        if r==1:
#            print (filee)
            shutil.copy(r'E:\F DRIVE\M.Tech\for assigning cl\selected\random 500_ll\\'+filee,r'E:\F DRIVE\M.Tech\for assigning cl\selected\mouse in random 500_ll\\'+filee)

print("--- %s seconds ---" % (time.time() - start_time))
