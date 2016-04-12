# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:12:27 2016

@author: Krishna
"""

import re
p = re.compile(ur'r\'(deficient\s.*?\sexhibited\s.*?\sgmk)\'')
test_str = "deficient dhte wagdg sdfs exhibited vlskdv gmk\n"
 
print re.search(p, test_str)