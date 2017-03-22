# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:27:17 2016

@author: chahat
"""

import os
import re
aa=open('results.txt', 'w')
keyword1 = open(r'/media/chahat/Krishna/F DRIVE/M.Tech/mouse_gs_small_simple_reduced.txt','r').readlines()  # this has the new small GS
keyword2 = open(r'/media/chahat/Krishna/F DRIVE/M.Tech/mouse_gs_number_large.txt','r').readlines()  # this has the large GS
#keyword1 = open('E:\F DRIVE\M.Tech\mouse_gs_small_simple_reduced.txt','r').readlines()  # this has the new small GS
#keyword2 = open('E:\F DRIVE\M.Tech\mouse_gs_number_large.txt','r').readlines()  # this has the large GS
keywords = keyword1+keyword2
keystripped = [k.rstrip().lower() for k in keywords]
for path, dirs, files in os.walk(r"/media/chahat/Krishna/F DRIVE/M.Tech/for assigning cl/mouse in series_ll"):
    i=0
    for file in files:
        i=i+1
        print ('%d' %(i))
        sentences = open(os.path.join(path,file), encoding='utf-8').readlines();
#        print (4)
#        r=0
        for s in sentences:
                s = s.rstrip()
                if s.startswith('!Series_title') or s.startswith('!Series_summary') or s.startswith('!Series_overall_design'):
                    s = s.lower()  
                    gs_list = [k for k in keystripped if k in s]
                    for g1 in gs_list:
                        #re.search(r'(%s\(control\))' %gs1, s1, re.I|re.S):
                        if re.search(r'%s\(control\)' %g1,s):
                            aa.write('%s(control)' %(g1))
#                            print ('%s(control)' %(g1) )
                            
aa.close()

#I RAN THIS CODE ON ALL MOUSE FILES IN THE 14K FILES, AND AFTER GOING THROUGH ALL OF THE 3378 FILES, THERE WERE '0' RESULTS.
#I CHECKED IF THE CODE WAS RIGHT AND IT WAS. SO THIS RULE IS BASICALLY USELESS.
#+++++++++++++++++++++++**************************++++++++++++++++++++++++++++