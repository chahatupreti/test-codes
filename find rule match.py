# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 19:44:22 2016

@author: Krishna
"""

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


rg1 = open(r'I:\My Online Documents\MTech\ruless occurence\keyword start.txt', 'w')
rg2 = open(r'I:\My Online Documents\MTech\ruless occurence\line start.txt', 'w')
rg3 = open(r'I:\My Online Documents\MTech\ruless occurence\fullstop.txt', 'w')
rg4 = open(r'I:\My Online Documents\MTech\ruless occurence\gs control.txt', 'w')
rg5 = open(r'I:\My Online Documents\MTech\ruless occurence\golden line.txt', 'w')
rg6 = open(r'I:\My Online Documents\MTech\ruless occurence\r four.txt', 'w')
rs1 = open(r'I:\My Online Documents\MTech\ruless occurence\minus one.txt', 'w')
rs2 = open(r'I:\My Online Documents\MTech\ruless occurence\minus two.txt', 'w')
rs3 = open(r'I:\My Online Documents\MTech\ruless occurence\plus one.txt', 'w')
ra1 = open(r'I:\My Online Documents\MTech\ruless occurence\activation one.txt', 'w')
ra2 = open(r'I:\My Online Documents\MTech\ruless occurence\activation two.txt', 'w')
ra3 = open(r'I:\My Online Documents\MTech\ruless occurence\activation three.txt', 'w')
ra4 = open(r'I:\My Online Documents\MTech\ruless occurence\activation four.txt', 'w')
rd1 = open(r'I:\My Online Documents\MTech\ruless occurence\deficient one.txt', 'w')
rd2 = open(r'I:\My Online Documents\MTech\ruless occurence\deficient two.txt', 'w')
rde1 = open(r'I:\My Online Documents\MTech\ruless occurence\deletion one.txt', 'w')
ri1 = open(r'I:\My Online Documents\MTech\ruless occurence\induced one.txt', 'w')
ri2 = open(r'I:\My Online Documents\MTech\ruless occurence\induced two.txt', 'w')
ri3 = open(r'I:\My Online Documents\MTech\ruless occurence\induced three.txt', 'w')
ri4 = open(r'I:\My Online Documents\MTech\ruless occurence\induced four.txt', 'w')
rin1 = open(r'I:\My Online Documents\MTech\ruless occurence\inhibition one.txt', 'w')
rk1 = open(r'I:\My Online Documents\MTech\ruless occurence\knockout one.txt', 'w')
rk2 = open(r'I:\My Online Documents\MTech\ruless occurence\knkockout two.txt', 'w')
rko1 = open(r'I:\My Online Documents\MTech\ruless occurence\ko.txt', 'w')
rm1 = open(r'I:\My Online Documents\MTech\ruless occurence\mutant one.txt', 'w')
rm2 = open(r'I:\My Online Documents\MTech\ruless occurence\mutant two.txt', 'w')
rn1 = open(r'I:\My Online Documents\MTech\ruless occurence\null.txt', 'w')
rr1 = open(r'I:\My Online Documents\MTech\ruless occurence\gmks start.txt', 'w')
rst1 = open(r'I:\My Online Documents\MTech\ruless occurence\stimulated one.txt', 'w')
rst2 = open(r'I:\My Online Documents\MTech\ruless occurence\stimulated two.txt', 'w')
rt1 = open(r'I:\My Online Documents\MTech\ruless occurence\\treated one.txt', 'w')
rt2 = open(r'I:\My Online Documents\MTech\ruless occurence\treated two.txt', 'w')
rs4 = open(r'I:\My Online Documents\MTech\ruless occurence\minus three.txt', 'w')
rs5 = open(r'I:\My Online Documents\MTech\ruless occurence\plus two.txt', 'w')
rs6 = open(r'I:\My Online Documents\MTech\ruless occurence\plus three.txt', 'w')






keyword1 = open('F:\M.Tech\mouse_gs_small_simple.txt','r').readlines()  # this has the small GS
keyword2 = open('F:\M.Tech\mouse_gs_number_large.txt','r').readlines()  # this has the large GS
keywords = keyword1+keyword2
#gmk = 'knockout'
c=0
def find_matches(s, gmk):
    #print("FINDMATCHES--- %s seconds ---" % (time.time() - start_time))
    r=0
    if gmk in s:  # checking if gmk is in the line
        l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', s) # split the line by comma, semicolon and space to check for gmks and gs. Also http://goo.gl/RPQNbT
        filter(None, l)       # remove empty elements in the list                  
        for gs in keywords: # gene symbols
           
            gs = gs.rstrip()     #remove lagging whitespace characters                   

            if gs in s: # search for GS in line. using 'gs in s' led to a lot of partial word matches
                gs1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gs)
                gs1=filter(None, gs1)
                gmk1 = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|-', gmk)
                gmk1=filter(None, gmk1)
                if any(l[i:i+len(gs1)]==gs1 for i in xrange(len(l)-len(gs1)+1)) and (any(l[i:i+len(gmk1)]==gmk1 for i in xrange(len(l)-len(gmk1)+1))): # this ensures that both gs and gmk are in l, as a unit(i.e. and in order) otherwise it was detecting things like 'beta c' from beta cells
                    k1 = "_KEYWORD_1_"
                    k2 = "_KEYWORD_2_"
                    text = s.replace(gmk, k1)  # because of this replacement, we dont have the problem of counting r from behind etc.
                    text = text.replace(gs, k2)
                    lt = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', text)
                    d_idx = {k1:[], k2:[]}
                    #print d_idx[k1]
                    for k,v in enumerate(lt):
                        if v == k1:
                            d_idx[k1].append(k)
                        elif v == k2:
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
                        print file
                        #print gs, gmk
                        #print "Number of occurences: ", len(data)
                        if data[i][0]<4:  # if r less than 4
                            rg6.write(file)
                            rg6.write('\n')
                            rg6.write (' r is %d ' % data[i][0])
                            rg6.write('\n')
                            rg6.write(gs)
                            rg6.write('\n')
                            rg6.write('Found %s in %s' % (gmk,s.strip()))
                            rg6.write('\n')
                    r=cl(s, gmk, gs, data)
                    #print r # tells how many times the rules function was called
                                





def cl(s1, gmk1, gs1, data1): # output will be the confidence level    
    #print("CL--- %s seconds ---" % (time.time() - start_time))    
    br0=''
    br3=''
    br=''
    s1=s1.replace(gs1, '_8MILLION8_')
    gs1='_8MILLION8_'
    #l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|"|\'|[()]|-', s)
    l = s1.split() 
    for ii in range(0,len(data1)):
        print 'loop'
        a = data1[ii]
        lo = min(a[1], a[2])
        hi = max(a[1], a[2])
        brr = l[max(0, lo-8):hi+8]
        br= " ".join(brr) 
        br00 = l[max(0, lo):hi+1]  # we dont need the 8 words here and there as the fullstop is between gmk1 and gs1
        br0= ' '.join(br00)
        br33 = l[max(0, lo-3):hi+3] 
        br3= ' '.join(br33)
    beg_gmk = ['over-activation', 'overexpression', 'loss of', 'knockout', 'haplo-insuffiency', 'haploinsufficiency', 'inactivation', 'knock-out', 'deletion', 'inhibition', 'knockdown', 'silencing']
    beg_other = ['Global gene expression', 'Gene expression profiling', 'Expression data', 'Gene expression analysis']
    for i in range(0,len(beg_gmk)):
        if re.search(r'(^!Series_.*?\s"%s)' %beg_gmk[i], s1, re.I|re.S):   # this rule looks optimum
            rr1.write(file)
            rr1.write('\n')
            rr1.write(gs1)
            rr1.write('\n')
            rr1.write('Found %s in %s' % (gmk1,s1.strip()))
            rr1.write('\n')

    for i in range(0,len(beg_other)):
        if re.search(r'(^!Series_.*?\s"%s)' %beg_other[i], s1, re.I|re.S):  # this rule looks optimum 
            rg2.write(file)
            rg2.write('\n')
            rg2.write(gs1)
            rg2.write('\n')
            rg2.write('Found %s in %s' % (gmk1,s1.strip()))
            rg2.write('\n')

    if re.search(r'(^!Series_\w.*?\s"Keywords:)', s1):
        ll=s1.split(',')
        v=0
        for i in range(0,len(ll)):
	     
           if gmk1 and gs1 in ll[i]:
               
               v=4 
               rg1.write(file)
               rg1.write('\n')
               rg1.write(gs1)
               rg1.write('\n')
               rg1.write('Found %s in %s' % (gmk1,s1.strip()))
               rg1.write('\n')        
        if v!=4:
           
           rg1.write('COMMA SEPARATED')
           rg1.write('\n')
           rg1.write(file)
           rg1.write('\n')
           rg1.write(gs1)
           rg1.write('\n')
           rg1.write('Found %s in %s' % (gmk1,s1.strip()))
           rg1.write('\n')
		
    if (re.search(r'(%s.*?\..*?%s)' % (re.escape(gs1), re.escape(gmk1)), br0, re.I|re.S)) or (re.search(r'(%s.*?\..*?%s)' % (re.escape(gmk1), re.escape(gs1)), br0, re.I|re.S)): #gs1 fullstop gmk1 and viceversa
        rg3.write(file)
        rg3.write('\n')
        rg3.write(gs1)
        rg3.write('\n')
        rg3.write('Found %s in %s' % (gmk1,s1.strip()))
        rg3.write('\n')
		
	
    if re.search(r'(%s\(control\))' %gs1, br3, re.I|re.S): #gs1(control)
        rg4.write(file)
        rg4.write('\n')
        rg4.write(gs1)
        rg4.write('\n')
        rg4.write('Found %s in %s' % (gmk1,s1.strip()))
        rg4.write('\n')
    if re.search(r'(The object of this study was to identify genes transcriptionally upregulated.*?downregulated)', s1):
        rg5.write(file)
        rg5.write('\n')
        rg5.write(gs1)
        rg5.write('\n')
        rg5.write('Found %s in %s' % (gmk1,s1.strip()))
        rg5.write('\n')

        
    if gmk1 == 'activation':
        if  re.search(r'(activation by %s)' %gs1, br0, re.I|re.S):
            ra1.write(file)
            ra1.write('\n')
            ra1.write(gs1)
            ra1.write('\n')
            ra1.write('Found %s in %s' % (gmk1,s1.strip()))
            ra1.write('\n')
        if  re.search(r'(probably\s.*?\s %s activation)' %gs1, br, re.I|re.S):
            ra2.write(file)
            ra2.write('\n')
            ra2.write(gs1)
            ra2.write('\n')
            ra2.write('Found %s in %s' % (gmk1,s1.strip()))
            ra2.write('\n')
        if  re.search(r'(critical for.*?%s activation)' %gs1, br, re.I|re.S):
            ra3.write(file)
            ra3.write('\n')
            ra3.write(gs1)
            ra3.write('\n')
            ra3.write('Found %s in %s' % (gmk1,s1.strip()))
            ra3.write('\n') 
        if  re.search(r'(%s.*?activation of)' %gs1, br3, re.I|re.S):
            ra4.write(file)
            ra4.write('\n')
            ra4.write(gs1)
            ra4.write('\n')
            ra4.write('Found %s in %s' % (gmk1,s1.strip()))
            ra4.write('\n')
    if gmk1 == 'deficient':
        if  re.search(r'(%s deficient)' %gs1, br0, re.I|re.S):
            rd1.write(file)
            rd1.write('\n')
            rd1.write(gs1)
            rd1.write('\n')
            rd1.write('Found %s in %s' % (gmk1,s1.strip()))
            rd1.write('\n')
        if  re.search(r'(deficient\s.*?\sexhibited\s.*?\s%s)' %gs1, br0, re.I|re.S):
            rd2.write(file)
            rd2.write('\n')
            rd2.write(gs1)
            rd2.write('\n')
            rd2.write('Found %s in %s' % (gmk1,s1.strip()))
            rd2.write('\n')
#    if gmk1 == 'deletion':
#        for all_gs in keywords:
            #all_gs=all_gs.rstrip()



#            if re.search(r'(\s%s-deletion\s.*?\s%s)' % (re.escape(all_gs), re.escape(gs1)), s1, re.I|re.S):
#                rde1.write(file)
#                rde1.write('\n')
#                rde1.write(gs1)
#                rde1.write('\n')
#                rde1.write('Found %s in %s' % (gmk1,s1.strip()))
#                rde1.write('\n')       
    if gmk1 == '-/-':
#        if r<3:
#            rs4.write(file)
#            rs4.write('\n')
#            rs4.write(gs1)
#           rs4.write('\n')
#            rs4.write('Found %s in %s' % (gmk1,s1.strip()))
#            rs4.write('\n')
        if  re.search(r'(-/-%s)' %gs1, br0, re.I|re.S):
            rs1.write(file)
            rs1.write('\n')
            rs1.write(gs1)
            rs1.write('\n')
            rs1.write('Found %s in %s' % (gmk1,s1.strip()))
            rs1.write('\n')
        if  re.search(r'(%s-/-)' %gs1, br0, re.I|re.S):
            rs2.write(file)
            rs2.write('\n')
            rs2.write(gs1)
            rs2.write('\n')
            rs2.write('Found %s in %s' % (gmk1,s1.strip()))
            rs2.write('\n')      
    if gmk1 == '+':
        if  re.search(r'(%s+)' %gs1, br0, re.I|re.S):
            rs3.write(file)
            rs3.write('\n')
            rs3.write(gs1)
            rs3.write('\n')
            rs3.write('Found %s in %s' % (gmk1,s1.strip()))
            rs3.write('\n')
        elif  re.search(r'(%s\(\+\))' %gs1, br3, re.I|re.S):
            rs5.write(file)
            rs5.write('\n')
            rs5.write(gs1)
            rs5.write('\n')
            rs5.write('Found %s in %s' % (gmk1,s1.strip()))
            rs5.write('\n')   
        else:
            rs6.write(file)
            rs6.write('\n')
            rs6.write(gs1)
            rs6.write('\n')
            rs6.write('Found %s in %s' % (gmk1,s1.strip()))
            rs6.write('\n')
    if gmk1 == 'induced':
        if  re.search(r'(%s.*?was shown\s.*?\sinduced)' %gs1, br0, re.I|re.S):
            ri1.write(file)
            ri1.write('\n')
            ri1.write(gs1)
            ri1.write('\n')
            ri1.write('Found %s in %s' % (gmk1,s1.strip()))
            ri1.write('\n')
        if  re.search(r'(%s.*?-induced)' %gs1, br0, re.I|re.S):
            ri2.write(file)
            ri2.write('\n')
            ri2.write(gs1)
            ri2.write('\n')
            ri2.write('Found %s in %s' % (gmk1,s1.strip()))
            ri2.write('\n')
        if  re.search(r'(induced.*?to %s)' %gs1, br0, re.I|re.S):
            ri3.write(file)
            ri3.write('\n')
            ri3.write(gs1)
            ri3.write('\n')
            ri3.write('Found %s in %s' % (gmk1,s1.strip()))
            ri3.write('\n') 
        if  re.search(r'(induced.*?while %s)' %gs1, br0, re.I|re.S):
            ri4.write(file)
            ri4.write('\n')
            ri4.write(gs1)
            ri4.write('\n')
            ri4.write('Found %s in %s' % (gmk1,s1.strip()))
            ri4.write('\n')
    if gmk1 == 'inhibition':
        if  re.search(r'(hypothesized\s.*?\sinhibition\s.*?\s%s )' %gs1, br, re.I|re.S):
            rin1.write(file)
            rin1.write('\n')
            rin1.write(gs1)
            rin1.write('\n')
            rin1.write('Found %s in %s' % (gmk1,s1.strip()))
            rin1.write('\n')
    if gmk1 == 'knockout':
        if  re.search(r'(effect of %s knockout)' %gs1, br3, re.I|re.S):
            rk1.write(file)
            rk1.write('\n')
            rk1.write(gs1)
            rk1.write('\n')
            rk1.write('Found %s in %s' % (gmk1,s1.strip()))
            rk1.write('\n')
        if  re.search(r'(double knockout)', br3, re.I|re.S): # for the time being
            rk2.write(file)
            rk2.write('\n')
            rk2.write(gs1)
            rk2.write('\n')
            rk2.write('Found %s in %s' % (gmk1,s1.strip()))
            rk2.write('\n')
    if gmk1 == 'KO':
        if  re.search(r'(double KO\W)', br3, re.I|re.S): # for the time being
            rko1.write(file)
            rko1.write('\n')
            rko1.write(gs1)
            rko1.write('\n')
            rko1.write('Found %s in %s' % (gmk1,s1.strip()))
            rko1.write('\n')
    if gmk1 == 'mutant':
        if  re.search(r'(harboring.*?%s mutant)' %gs1, br3, re.I|re.S):
            rm1.write(file)
            rm1.write('\n')
            rm1.write(gs1)
            rm1.write('\n')
            rm1.write('Found %s in %s' % (gmk1,s1.strip()))
            rm1.write('\n')
        if  re.search(r'(mutant.*?causes.*?%s)' %gs1, br0, re.I|re.S):
            rm2.write(file)
            rm2.write('\n')
            rm2.write(gs1)
            rm2.write('\n')
            rm2.write('Found %s in %s' % (gmk1,s1.strip()))
            rm2.write('\n')
#    if gmk1 == 'null':
#        for all_gs in keywords:
            #all_gs=all_gs.rstrip()
#            if re.search(r'(matched %s\s.*?\s%s.*?null)' % (re.escape(gs1), re.escape(all_gs)), s, re.I|re.S): #doing %gs1, %all_gs gave syntax error. THIS NEW WAY IS THE RIGHT WAY TO DO IT
#                rn1.write(file)
#                rn1.write('\n')
#                rn1.write(gs1)
#                rn1.write('\n')
#                rn1.write('Found %s in %s' % (gmk1,s.strip()))
#                rn1.write('\n')
    if gmk1 == 'stimulated':
        if  re.search(r'(.*?-stimulated.*?%s)' %gs1, br, re.I|re.S):
            rst2.write(file)
            rst2.write('\n')
            rst2.write(gs1)
            rst2.write('\n')
            rst2.write('Found %s in %s' % (gmk1,s1.strip()))
            rst2.write('\n')
        if  re.search(r'(%s-stimulated)' %gs1, br0, re.I|re.S):
            rst1.write(file)
            rst1.write('\n')
            rst1.write(gs1)
            rst1.write('\n')
            rst1.write('Found %s in %s' % (gmk1,s1.strip()))
            rst1.write('\n')
    if gmk1 == 'treated':
        if  re.search(r'(treated.*?control.*?%s)' %gs1, br0, re.I|re.S):
            rt1.write(file)
            rt1.write('\n')
            rt1.write(gs1)
            rt1.write('\n')
            rt1.write('Found %s in %s' % (gmk1,s1.strip()))
            rt1.write('\n')
        if  re.search(r'(control or %s-treated)' %gs1, br3, re.I|re.S):
            rt2.write(file)
            rt2.write('\n')
            rt2.write(gs1)
            rt2.write('\n')
            rt2.write('Found %s in %s' % (gmk1,s1.strip()))
            rt2.write('\n')
    return 4        





    
c=0
print 1
for path, dirs, files in os.walk('I:\My Online Documents\MTech\series_imp_info'):
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
                if s.startswith('!Series_title') or s.startswith('!Series_summary') or s.startswith('!Series_overall_design'):
                    for gmk in a:
                        gmk = gmk.rstrip() #to remove the lagging \n in many GMKs
                        find_matches(s, gmk)

print("--- %s seconds ---" % (time.time() - start_time))
      
          
    


