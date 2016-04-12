# -*- coding: utf-8 -*-
"""
Created on Sat Jan 02 18:16:16 2016

@author: Krishna
"""

import os
import re
import time
start_time = time.time()
q=open('C:\Users\Krishna\Desktop\up down analysis for orgs\gmk_gs vicinity_large_iddle.txt','w')
a = open('F:\M.Tech\patterns for gmk_down.txt','r').readlines()
a1 = open('F:\M.Tech\patterns for gmk_up.txt','r').readlines()
a=a+a1
#print a
keywords = open('F:\M.Tech\mouse_gs_number_large.txt','r').readlines()  # this has the large gs's
#gmk = 'knockout'
def find_matches(s, gmk):
    r=0
    if gmk in s:  # checking if gmk is in the line
        l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', s) # split the line by comma, semicolon and space to check for gmks and gs. Also http://goo.gl/RPQNbT
        l=filter(None, l)                        
        if gmk == '-/-':
            q.write(gmk)
            for gs in keywords: # gene symbols
                        
                gs = gs.rstrip()     #remove lagging whitespace characters                   
                if gs == 'Th':
                    print gs
                    #print l
                    if gs in s: # search for GS in line. using 'gs in s' led to a lot of partial word matches
                        print 'eeeeeeeee'
                        gs1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gs)
                        gs1=filter(None, gs1)
                        gs1=gs1[0]
                        gmk1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gmk)
                        gmk1=filter(None, gmk1)
                        gmk1=gmk1[0]
                        print gmk, gmk1
                        if (gs1 in l) and (gmk1 in l):
                        #if (gmk in s): # ensure both are in the list. sometimes, they are not because of some attached delimiters                                                                                                     
        #                                    index = s.find(gs) #find index of the GS in the line
        #                                    if (s[index-1].isalpha() or s[index+len(gs)+1].isalpha())==False: #see if the 2 characters preceding and succeeding the GS are not alphabets. this is imp because if they are, then we dont want it, cause it means the GS is within a word
                            r = abs(l.index(gs1) - l.index(gmk1)) # find distance between first character of gs and gmk
                            #print 'title %d' % r                                     
                            if r<=8:
                                q.write(file)
                                q.write('\n')
                                q.write(gs)
                                q.write (' r is %d ' % r)
                                q.write('\n')
                                q.write('Found %s in %s' % (gmk,s.strip()))
                                q.write('\n')
    
c=0
for path, dirs, files in os.walk('F:\M.Tech\org segregated\mus musculus\st'):
    for file in files:
        sentences = open(os.path.join(path,file),'r').readlines();
        c = c+1
        r=0
        print c # one value printed for each file
        #print file
        print("--- %s seconds ---" % (time.time() - start_time))
        k=0
        hg=0
        for gmk in a:
            gmk = gmk.rstrip() #to remove the lagging \n in many GMKs
            #print gmk
            for s in sentences:
                s = s.rstrip()
                if s.startswith('!Series_title'):
                    find_matches(s, gmk)                   
                if s.startswith('!Series_summary'):
                    find_matches(s, gmk)
                if s.startswith('!Series_overall_design'):
                    find_matches(s, gmk)
q.close()
print("--- %s seconds ---" % (time.time() - start_time))         

      
          
    
