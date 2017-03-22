#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
for path, dirs, files in os.walk(r'F:\M.Tech\for assigning cl\series_imp_info_l'):
    for file in files:
        sentences = open(os.path.join(path,file),'r').readlines()
        for s in sentences:
        			# SEARCHING FOR ALPHA SYMBOL
        	# if  re.search(r'α',s):
        	# 	print file
            
        			# SEARCHING FOR EXPERIMENT TYPES
			s=s.rstrip()
			if s.startswith('!Series_type'):
				print s, file