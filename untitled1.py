# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:23:54 2015

@author: Krishna
"""

def count_string_occurrence(org):
    f = open('D:\M.Tech work\qfilter_output matches.txt','r')
    contents = f.read()
    f.close()
    #print  org,
    print contents.count(org)

read_f = open('D:\M.Tech work\unique filter matches from qfilter.txt','r')
for line in read_f:
    count_string_occurrence(line)
read_f.close()
