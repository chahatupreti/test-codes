# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 11:37:35 2016

@author: Krishna
"""
import os
q=open('C:\Users\Krishna\Desktop\cc.txt','w')

qq=open('C:\Users\Krishna\Desktop\cvc.txt','w')

for path, dirs, files in os.walk('I:\My Online Documents\MTech\GEO_website\series\old series files'):
    for file in files:
        q.write(file)
        q.write('\n')        
for path, dirs, files in os.walk('F:\M.Tech\series_imp_info'):
    for file in files:
        qq.write(file)
        qq.write('\n')        