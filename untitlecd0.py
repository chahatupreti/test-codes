# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 12:08:54 2016

@author: Krishna
"""
import re
r = 'for the (Th-/-) of'
gmk='-/-'
l=re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', r)
l1=re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', r)
al=re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', gmk)
al1=re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gmk)
print l
print l1
print al
print al1