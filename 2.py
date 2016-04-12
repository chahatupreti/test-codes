# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:55:49 2016

@author: Krishna
"""

import re
s = 'there is a good boy in this room this'
fg = 'this'
s=re.sub(fg, '8mil', s, flags=re.I)
print s