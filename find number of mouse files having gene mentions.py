# -*- coding: utf-8 -*-
"""
Created on Thu Sep 08 19:23:02 2016

@author: Krishna
"""
import os
import re
# keyword1 = open('E:\F DRIVE\M.Tech\mouse_gs_small_simple_reduced.txt','r').readlines()  # this has the new small GS
# keyword2 = open('E:\F DRIVE\M.Tech\mouse_gs_number_large.txt','r').readlines()  # this has the large GS
# keywords = keyword1+keyword2
keywords = open('E:\F DRIVE\M.Tech\etc\ms.txt').readlines()
keystripped = [k.rstrip().lower() for k in keywords]
# for kk in keystripped:
#     kk = re.escape(kk)
c=0
for path, dirs, files in os.walk(r'E:\F DRIVE\M.Tech\for assigning cl\mouse in series_ll'):                    
    for file in files:
        # print (file)
        sentences = open(os.path.join(path,file), encoding = 'utf-8').readlines();
        for s in sentences:
            for k in keystripped:
                # print (k)
#                if  re.search(r'(%s.*?activation of)' %k, s, re.I|re.S):
                if re.search(r'(\b%s\b)' %k, s, re.I):
                    c=c+1
                    print (k)
                    print(file)
                    break
            else:
                continue
            break
print (c)
#if re.search(r'(^\W*(?:\w+\W+){0,6}%s\b)' %gs1, s1, re.I|re.S):
#if re.search(r'([\.] here(,)? we[^\.]*?( |\()%s)' %gs1, s1) : #
#if  re.search(r'(%s.*?activation of)' %gs1, br3, re.I|re.S):