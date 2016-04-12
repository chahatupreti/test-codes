# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:27:38 2016

@author: Krishna
"""
import re
s = '+ is a pretty good boy +'
gmk = '+'
k1 = 'dd'
text = re.sub(re.escape(gmk), k1, s, flags=re.I)
print text