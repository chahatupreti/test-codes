# -*- coding: utf-8 -*-
"""
Created on Thu Dec 03 14:18:54 2015

@author: Krishna
"""

f=open('F:\M.Tech\org segregated\Arabidopsis thaliana\GSE10326_series_matrix.txtimp_info.txt','r')
s = f.readlines()
d = 'analysis of'
for sw in s:
    if d in sw:
        print 'got it'