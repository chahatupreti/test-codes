# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:56:07 2016

@author: Krishna
"""
import re
w=open(r'C:\Users\Krishna\Desktop\up down analysis for orgs\test.txt', 'r').readlines()
for i in range(0, len(w)):
    s=w[i]
    if re.search(r'(The object of this study was to identify genes transcriptionally upregulated.*?downreiigulated)', s):
        print 5