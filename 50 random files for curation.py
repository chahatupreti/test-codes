# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 01:15:11 2016

@author: Krishna
"""
import os
import random
import shutil
c=[]
i=0
# for path, dirs, files in os.walk(r'E:\F DRIVE\M.Tech\for assigning cl\series_imp_info_ll'):
#     for file in files:
#         c.append(file)
a=open(r'C:\Users\Krishna\Desktop\ALL\up down analysis for orgs\here_we file matches_mouse_noncurated.txt').readlines()
# print c        
c1=random.sample(a,50)
# print (c1)
for c11 in c1:
    # shutil.copy(r'E:\F DRIVE\M.Tech\for assigning cl\series_imp_info_ll\\'+c11,r'E:\F DRIVE\M.Tech\for assigning cl\selected\random 500_ll\\'+c11)
    print(c11)