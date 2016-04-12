# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 19:15:21 2016

@author: Krishna
"""
import re
text = 'aquaporin protein-1 the flory of gthys inhibition in this proffession by in aquaporin protein-1 its inhibition b , aquaporin protein-1'
a = 'aquaporin protein-1'
b = 'inhibition'
k1 = "_KEYWORD_1_"
k2 = "_KEYWORD_2_"
text = text.replace(a, k1)
text = text.replace(b, k2)
l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|"|\'|[()]|-', text)
l=filter(None,l)
#print l
d_idx = {k1:[], k2:[]}
print d_idx[k1]
for k,v in enumerate(l):
    if v == k1:
        d_idx[k1].append(k)
    elif v == k2:
        d_idx[k2].append(k)
print d_idx[k2]
distance = 5
data = []
for idx1 in d_idx[k1]:
    for idx2 in d_idx[k2]:
        d = abs(idx1 - idx2)
        if d<=distance:
            data.append((d,idx1,idx2))
            
data.sort(key=lambda x: x[0])
print data
print l
print "Least distance: ", data[0][0]
print "Index of kw1 and kw2: ", data[0][1:]
print "Number of occurences: ", len(data)
for i in range(0,len(data)):
    a = data[i]
    lo = min(a[1], a[2])
    hi = max(a[1], a[2])
    br =  l[max(0, lo-8):hi+8]