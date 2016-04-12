# -*- coding: utf-8 -*-
"""
Created on Fri Jan 08 18:18:35 2016

@author: Krishna
"""

text = 'aquaporin protein-1 the flory of gthys inhibition in this proffession by in aquaporin protein-1  its inhibition b'
a = 'aquaporin protein-1'
b = 'inhibition'
text = text.replace(a, 'k1')
text = text.replace(b, 'k2')
l = text.split()
print l
print 'k1 -> %s' % a
print 'k2 -> %s' % b

last_a = -1
last_b = -1
counts = 0
max_match_tuple = (6,0)  # Initialize it like this since you want to track proximity less than 5
for k,v in enumerate(l):
        #print str(k) + '--->' + str(v)
        if v == 'k1':
                last_a = k
                if k - last_b < 6 and last_b != -1:
                        counts = counts + 1
                        if k - last_b < max_match_tuple[0] - max_match_tuple[1]:
                             max_match_tuple = (k, last_b)
        if v == 'k2':
                last_b = k
                if k - last_a < 6 and last_a != -1:
                        counts = counts + 1
                        if k - last_a < max_match_tuple[0] - max_match_tuple[1]:
                             max_match_tuple = (k, last_a)  # Careful with the order here since it matters for above substruction 
print counts
print max_match_tuple