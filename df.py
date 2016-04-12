# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 18:43:15 2016

@author: Krishna
"""

import os
import re
import time
start_time = time.time()
#q=open('C:\Users\Krishna\Desktop\up down analysis for orgs\checking rules.txt','w')
a = open('F:\M.Tech\patterns for gmk_down.txt','r').readlines()
a1 = open('F:\M.Tech\patterns for gmk_up.txt','r').readlines()
a=a+a1


rg1 = open(r'L:\My Online Documents\MTech\ruless occurence\keyword start7.txt', 'w')
rg2 = open(r'L:\My Online Documents\MTech\ruless occurence\line start7.txt', 'w')
rg3 = open(r'L:\My Online Documents\MTech\ruless occurence\fullstop.txt', 'w')
rg4 = open(r'L:\My Online Documents\MTech\ruless occurence\gs control.txt', 'w')
rg5 = open(r'L:\My Online Documents\MTech\ruless occurence\golden line7.txt', 'w')
rg6 = open(r'L:\My Online Documents\MTech\ruless occurence\r four.txt', 'w')
rs1 = open(r'L:\My Online Documents\MTech\ruless occurence\minus one.txt', 'w')
rs2 = open(r'L:\My Online Documents\MTech\ruless occurence\minus two.txt', 'w')
rs3 = open(r'L:\My Online Documents\MTech\ruless occurence\plus one.txt', 'w')
ra1 = open(r'L:\My Online Documents\MTech\ruless occurence\activation one.txt', 'w')
ra2 = open(r'L:\My Online Documents\MTech\ruless occurence\activation two.txt', 'w')
ra3 = open(r'L:\My Online Documents\MTech\ruless occurence\activation three.txt', 'w')
ra4 = open(r'L:\My Online Documents\MTech\ruless occurence\activation four.txt', 'w')
rd1 = open(r'L:\My Online Documents\MTech\ruless occurence\deficient one.txt', 'w')
rd2 = open(r'L:\My Online Documents\MTech\ruless occurence\deficient two.txt', 'w')
rde1 = open(r'L:\My Online Documents\MTech\ruless occurence\deletion one.txt', 'w')
ri1 = open(r'L:\My Online Documents\MTech\ruless occurence\induced one.txt', 'w')
ri2 = open(r'L:\My Online Documents\MTech\ruless occurence\induced two.txt', 'w')
ri3 = open(r'L:\My Online Documents\MTech\ruless occurence\induced three.txt', 'w')
ri4 = open(r'L:\My Online Documents\MTech\ruless occurence\induced four.txt', 'w')
rin1 = open(r'L:\My Online Documents\MTech\ruless occurence\inhibition one.txt', 'w')
rk1 = open(r'L:\My Online Documents\MTech\ruless occurence\knockout one.txt', 'w')
rk2 = open(r'L:\My Online Documents\MTech\ruless occurence\knkockout two7.txt', 'w')
rko1 = open(r'L:\My Online Documents\MTech\ruless occurence\ko7.txt', 'w')
rm1 = open(r'L:\My Online Documents\MTech\ruless occurence\mutant one.txt', 'w')
rm2 = open(r'L:\My Online Documents\MTech\ruless occurence\mutant two.txt', 'w')
rn1 = open(r'L:\My Online Documents\MTech\ruless occurence\null.txt', 'w')
rr1 = open(r'L:\My Online Documents\MTech\ruless occurence\gmks start7.txt', 'w')
rst1 = open(r'L:\My Online Documents\MTech\ruless occurence\stimulated one.txt', 'w')
rst2 = open(r'L:\My Online Documents\MTech\ruless occurence\stimulated two.txt', 'w')
rt1 = open(r'L:\My Online Documents\MTech\ruless occurence\\treated one.txt', 'w')
rt2 = open(r'L:\My Online Documents\MTech\ruless occurence\treated two.txt', 'w')
rs4 = open(r'L:\My Online Documents\MTech\ruless occurence\minus three7.txt', 'w')
rs5 = open(r'L:\My Online Documents\MTech\ruless occurence\plus two.txt', 'w')
rs6 = open(r'L:\My Online Documents\MTech\ruless occurence\plus three.txt', 'w')
#rrr = open(r'L:\My Online Documents\MTech\goodthree.txt', 'w')





keyword1 = open('F:\M.Tech\mouse_gs_small_simple.txt','r').readlines()  # this has the small GS
keyword2 = open('F:\M.Tech\mouse_gs_number_large.txt','r').readlines()  # this has the large GS
keywords = keyword1+keyword2
#keywords = ['gs', 'gss']
c=0

def find_matches(s, gmk):
    #print 's and gmk are'
    #print s,gmk
    #print("FINDMATCHES--- %s seconds ---" % (time.time() - start_time))
    
    if gmk in s:  # checking if gmk is in the line
        l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', s) # split the line by comma, semicolon and space to check for gmks and gs. Also http://goo.gl/RPQNbT
        filter(None, l)       # remove empty elements in the list   
        gs_list=[] 
        for gss in keywords:
                gss=gss.rstrip()
                gss=gss.lower()
                if gss in s:
                    gs_list.append(gss)              
        for gs in gs_list: # gene symbols
            #rrr.write('\n')            
            #rrr.write(gs)
            if gs in s: # search for GS in line. using 'gs in s' led to a lot of partial word matches
                gs1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gs)
                gs1=filter(None, gs1)
                gmk1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gmk)
                gmk1=filter(None, gmk1)
                if any(l[i:i+len(gs1)]==gs1 for i in xrange(len(l)-len(gs1)+1)) and (any(l[i:i+len(gmk1)]==gmk1 for i in xrange(len(l)-len(gmk1)+1))): # this ensures that both gs and gmk are in l, as a unit(i.e. and in order) otherwise it was detecting things like 'beta c' from beta cells
                    #  UPTO THIS POINT WE HAVE ESTABLISHED THAT THE GMK AND GS ARE INDEED IN THE LINE                    
                    k1 = '_MKKEYWORD_1_'
                    k2 = '_SKEYWORD_2_'
                    #print gmk
                    text = re.sub(re.escape(gmk), k1, s, flags=re.I) # because of this replacement, we dont have the problem of counting r from behind etc.
                                                # also, I cannot use the regex based replacement used below for gmk replacement because we do want 
                                                # cases where gmk's like -/- or + are just after or before a word, without the word boundary   
                    text = re.sub(r'(\b%s\b)' % (re.escape(gs)), k2, text, flags=re.I)
                    #text = s.replace(gmk, k1)
                    #text = text.replace(gs, k2)
                    #print text
                    lt = text.split()                    
                    #lt = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', text)
                    d_idx = {k1:[], k2:[]}
                    #print d_idx[k1]
                    for k,v in enumerate(lt):
                        if k1 in v:
                            d_idx[k1].append(k)
                        if k2 in v:
                            d_idx[k2].append(k)
                    distance = 8
                    data = []
                    for idx1 in d_idx[k1]:
                        for idx2 in d_idx[k2]:
                            d = abs(idx1 - idx2)
                            if d<=distance:
                                data.append((d,idx1,idx2))
                                
                    data.sort(key=lambda x: x[0])
                    for i in range (0, len(data)):  
                        #print "Least distance: ", data[0][0]
                        #print file
                        #print gs, gmk
                        #print "Number of occurences: ", len(data)
                        aq = data[i]
                        loq = min(aq[1], aq[2])
                        hiq = max(aq[1], aq[2])
                        brrq = lt[max(0, loq-6):hiq+6]
                        brq = " ".join(brrq) 
                        
                        if data[i][0]<4:  # if r less than 4
                            rg6.write(file)
                            rg6.write('\n')
                            rg6.write (' r is %d ' % data[i][0])
                            rg6.write('\n')
                            rg6.write(gs)
                            rg6.write('\n')
                            rg6.write(gmk)
                            rg6.write('\n')
                            rg6.write(brq)
                            rg6.write('\n')
                            rg6.write('Found %s in %s' % (gmk,s.strip()))
                            rg6.write('\n')
                    if data: 
                        cl(s, gmk, gs, gs_list, data)
                        


def closef():
    rg1.close()
    rg2.close()
    rg3.close()
    rg4.close()
    rg5.close() 
    rg6.close() 
    rs1.close() 
    rs2.close() 
    rs3.close() 
    ra1.close()
    ra2.close() 
    ra3.close()
    ra4.close()
    rd1.close()
    rd2.close()
    rde1.close()
    ri1.close()
    ri2.close()
    ri3.close() 
    ri4.close()
    rin1.close()
    rk1.close()
    rk2.close() 
    rko1.close()
    rm1.close()
    rm2.close()
    rn1.close()
    rr1.close() 
    rst1.close()
    rst2.close()
    rt1.close()
    rt2.close() 
    rs4.close()
    rs5.close()
    rs6.close() 
    #rrr.close()
            

    
c=0
for path, dirs, files in os.walk(r'L:\My Online Documents\MTech\sii temp\temper'):
    for file in files:
        sentences = open(os.path.join(path,file),'r').readlines();
        c = c+1
        r=0
        print c # one value printed for each file
        #print file
        print("--- %s seconds ---" % (time.time() - start_time))
        k=0
        hg=0
        for s in sentences:
            s = s.rstrip()
            s = s.lower()
#            gs_list=[]
#            for gss in keywords:
#                gss=gss.rstrip()
#                if gss in s:
#                    gs_list.append(gss)
            #if s.startswith('!series_title') or s.startswith('!Series_summary') or s.startswith('!Series_overall_design'):
            if s.startswith('!series_title') or s.startswith('!series_summary') or s.startswith('!series_overall_design'):    
                for gmk in a:
                    gmk = gmk.rstrip() #to remove the lagging \n in many GMKs
                    gmk = gmk.lower()
                    find_matches(s, gmk)
closef()
print("--- %s seconds ---" % (time.time() - start_time))
      
          
    
