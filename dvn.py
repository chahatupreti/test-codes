# -*- coding: utf-8 -*-
"""
Created on Tue Jan 05 18:43:15 2016

@author: Krishna
"""
from collections import Counter
import os
import re
import time
start_time = time.time()
#q=open('C:\Users\Krishna\Desktop\up down analysis for orgs\checking rules.txt','w')
a = open('F:\M.Tech\patterns for gmk_down.txt','r').readlines()
a1 = open('F:\M.Tech\patterns for gmk_up.txt','r').readlines()
a=a+a1


rg1 = open(r'L:\My Online Documents\MTech\rules occurence\keyword start7.txt', 'w')
rg2 = open(r'L:\My Online Documents\MTech\rules occurence\line start7.txt', 'w')
rg3 = open(r'L:\My Online Documents\MTech\rules occurence\fullstop.txt', 'w')
rg4 = open(r'L:\My Online Documents\MTech\rules occurence\gs control.txt', 'w')
rg5 = open(r'L:\My Online Documents\MTech\rules occurence\golden line7.txt', 'w')
rg6 = open(r'L:\My Online Documents\MTech\rules occurence\r four.txt', 'w')
rs1 = open(r'L:\My Online Documents\MTech\rules occurence\minus one.txt', 'w')
rs2 = open(r'L:\My Online Documents\MTech\rules occurence\minus two.txt', 'w')
rs3 = open(r'L:\My Online Documents\MTech\rules occurence\plus one.txt', 'w')
ra1 = open(r'L:\My Online Documents\MTech\rules occurence\activation one.txt', 'w')
ra2 = open(r'L:\My Online Documents\MTech\rules occurence\activation two.txt', 'w')
ra3 = open(r'L:\My Online Documents\MTech\rules occurence\activation three.txt', 'w')
ra4 = open(r'L:\My Online Documents\MTech\rules occurence\activation four.txt', 'w')
rd1 = open(r'L:\My Online Documents\MTech\rules occurence\deficient one.txt', 'w')
rd2 = open(r'L:\My Online Documents\MTech\rules occurence\deficient two.txt', 'w')
rde1 = open(r'L:\My Online Documents\MTech\rules occurence\deletion one.txt', 'w')
ri1 = open(r'L:\My Online Documents\MTech\rules occurence\induced one.txt', 'w')
ri2 = open(r'L:\My Online Documents\MTech\rules occurence\induced two.txt', 'w')
ri3 = open(r'L:\My Online Documents\MTech\rules occurence\induced three.txt', 'w')
ri4 = open(r'L:\My Online Documents\MTech\rules occurence\induced four.txt', 'w')
rin1 = open(r'L:\My Online Documents\MTech\rules occurence\inhibition one.txt', 'w')
rk1 = open(r'L:\My Online Documents\MTech\rules occurence\knockout one.txt', 'w')
rk2 = open(r'L:\My Online Documents\MTech\rules occurence\knkockout two7.txt', 'w')
rko1 = open(r'L:\My Online Documents\MTech\rules occurence\ko7.txt', 'w')
rm1 = open(r'L:\My Online Documents\MTech\rules occurence\mutant one.txt', 'w')
rm2 = open(r'L:\My Online Documents\MTech\rules occurence\mutant two.txt', 'w')
rn1 = open(r'L:\My Online Documents\MTech\rules occurence\null.txt', 'w')
rr1 = open(r'L:\My Online Documents\MTech\rules occurence\gmks start7.txt', 'w')
rst1 = open(r'L:\My Online Documents\MTech\rules occurence\stimulated one.txt', 'w')
rst2 = open(r'L:\My Online Documents\MTech\rules occurence\stimulated two.txt', 'w')
#rt1 = open(r'L:\My Online Documents\MTech\rules occurence\\treated one.txt', 'w')
rt2 = open(r'L:\My Online Documents\MTech\rules occurence\treated two.txt', 'w')
rs4 = open(r'L:\My Online Documents\MTech\rules occurence\minus three7.txt', 'w')
rs5 = open(r'L:\My Online Documents\MTech\rules occurence\plus two.txt', 'w')
rs6 = open(r'L:\My Online Documents\MTech\rules occurence\plus three.txt', 'w')
#rrr = open(r'L:\My Online Documents\MTech\goodthree.txt', 'w')





keyword0 = open('F:\M.Tech\mus musculus_genes_only.txt','r').readlines()
keyword1 = open('F:\M.Tech\mus musculus_aliases_only.txt','r').readlines()  
keyword2 = open('F:\M.Tech\mus musculus_description_only.txt','r').readlines()  
keyword3 = open('F:\M.Tech\mus musculus_other_designation_only.txt','r').readlines()
z = open('C:\Users\Krishna\Desktop\up down analysis for orgs\GS to remove.txt','r').readlines()
z=Counter(z)
keyword0=Counter(keyword0)
keyword0=list(keyword0-z)   # this is how you subtract two lists. (http://stackoverflow.com/a/2071172/4169943)
keyword1=Counter(keyword1)
keyword1=list(keyword1-z)
keyword2=Counter(keyword2)
keyword2=list(keyword2-z)
keyword3=Counter(keyword3)
keyword3=list(keyword3-z)
 
kk=[[] for x in xrange(4)]
kk[0]=keyword0
kk[1]=keyword1
kk[2]=keyword2
kk[3]=keyword3
#keywords = keyword1+keyword2
#keywords = ['gs', 'gss']
c=0

def find_matches(s, gmk):
    
    if gmk in s:  # checking if gmk is in the line
        l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|[()]|-', s) # split the line by comma, semicolon and space to check for gmks and gs. Also http://goo.gl/RPQNbT
        filter(None, l)       # remove empty elements in the list   
        gs_list0=[]
        gs_list1=[]
        gs_list2=[]
        gs_list3=[]
        gkk=[[] for x in xrange(4)]
        gkk[0]=gs_list0
        gkk[1]=gs_list1
        gkk[2]=gs_list2
        gkk[3]=gs_list3
        for ic in range(0,len(kk)):
            
            for gss in kk[ic]:
                    gss=gss.rstrip()
                    gss=gss.lower()
                    if gss in s:
                        gkk[ic].append(gss)              
            for gs in gkk[ic]: # gene symbols
               
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
                        text = re.sub(r'(\b%s\b)' % (re.escape(gs)), k2, text, flags=re.I) #ensure GS isn't within another word, something hat won't happen for a GMK
                     
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
                           
                            aq = data[i]
                            loq = min(aq[1], aq[2])
                            hiq = max(aq[1], aq[2])
                            brrq = lt[max(0, loq-6):hiq+6]
                            brq = " ".join(brrq) 
                            
                            if data[i][0]<4:  # if r less than 4
                                rg6.write(str(ic))
                                rg6.write('\t')                            
                                rg6.write(file)
                                rg6.write('\t')
                                rg6.write (' r is %d ' % data[i][0])
                                rg6.write('\t')
                                rg6.write(gs)
                                rg6.write('\t')
                                rg6.write(gmk)
                                rg6.write('\t')
                                rg6.write(brq)
                                rg6.write('\t')
                                rg6.write('Found %s in %s' % (gmk,s.strip()))
                                rg6.write('\n')
                        if data: 
                            cl(s, gmk, gs, gkk[ic], data, ic)
                        
def cl(s1, gmk1, gs1, gs_list1, data1, icc): # output will be the confidence level    
    icc=str(icc)  
    gs11=gs1 # saving the GS to display in the final file
    br0=''
    br3=''
    br=''
    gs_list1.remove(gs1) # AS WE WANT TO USE THIS LIST FOR GETTING THE GS'S THAT ARE APART FROM THE CURRENT GS        
    s1 = re.sub(r'(\b(%s)\b)' % (gs1), r'_8MILLION8_', s1, flags=re.I) # inserts the token wherever there is GS. The \b before & after ensures this doesnt happen in between words

    gs1='_8MILLION8_'
    l = s1.split()  # i switched from the complex split above to just space split to ensure that the splitters can be part of a rule
    
    beg_gmk = ['over-activation', 'overexpression', 'loss of', 'knockout', 'haplo-insuffiency', 'haploinsufficiency', 'inactivation', 'knock-out', 'deletion', 'inhibition', 'knockdown', 'silencing']
    beg_other = ['Global gene expression', 'Gene expression profiling', 'Expression data', 'Gene expression analysis']
    for i in range(0,len(beg_gmk)):
        if re.search(r'(^!Series_.*?\s"%s)' %beg_gmk[i], s1, re.I|re.S):   # this rule looks optimum
            rr1.write(icc)
            rr1.write('\t')
            rr1.write(file)
            rr1.write('\t')
            rr1.write(gs11)
            rr1.write('\t')
            rr1.write('Found %s in %s' % (gmk1,s1.strip()))
            rr1.write('\n')

    for i in range(0,len(beg_other)):
        if re.search(r'(^!Series_.*?\s"%s)' %beg_other[i], s1, re.I|re.S):  # this rule looks optimum 
            rg2.write(icc)
            rg2.write('\t')
            rg2.write(file)
            rg2.write('\t')
            rg2.write(gs11)
            rg2.write('\t')
            rg2.write('Found %s in %s' % (gmk1,s1.strip()))
            rg2.write('\n')

    if re.search(r'(^!Series_\w.*?\s"Keywords:)', s1):
        ll=s1.split(',')
        v=0
        for i in range(0,len(ll)):
	     
           if gmk1 and gs1 in ll[i]:
               
               v=4
               rg1.write(icc)
               rg1.write('\t')
               rg1.write(file)
               rg1.write('\t')
               rg1.write(gs11)
               rg1.write('\t')
               rg1.write('Found %s in %s' % (gmk1,s1.strip()))
               rg1.write('\n')        
        if v!=4:
           rg1.write(icc)
           rg1.write('\t')
           rg1.write('COMMA SEPARATED')
           rg1.write('\t')
           rg1.write(file)
           rg1.write('\t')
           rg1.write(gs11)
           rg1.write('\t')
           rg1.write('Found %s in %s' % (gmk1,s1.strip()))
           rg1.write('\n')
			
	
    if re.search(r'(%s\(control\))' %gs1, s1, re.I|re.S): #gs1(control)
        rg4.write(icc)
        rg4.write('\t')        
        rg4.write(file)
        rg4.write('\t')
        rg4.write(gs11)
        rg4.write('\t')
        rg4.write('Found %s in %s' % (gmk1,s1.strip()))
        rg4.write('\n')
    if re.search(r'(The object of this study was to identify genes transcriptionally upregulated.*?downregulated)', s1):
        rg5.write(icc)
        rg5.write('\t')        
        rg5.write(file)
        rg5.write('\t')
        rg5.write(gs11)
        rg5.write('\t')
        rg5.write('Found %s in %s' % (gmk1,s1.strip()))
        rg5.write('\n')
 
    
    
    for ii in range(0,len(data1)):
        #print 'loop'
        a = data1[ii]
        lo = min(a[1], a[2])
        hi = max(a[1], a[2])
        brr = l[max(0, lo-6):hi+6]
        br= " ".join(brr) 
        br00 = l[max(0, lo):hi+1]  # we dont need the 8 words here and there as the fullstop is between gmk1 and gs1
        br0= ' '.join(br00)
        br33 = l[max(0, lo-3):hi+3] 
        br3= ' '.join(br33)
               
        if (re.search(r'(%s.*?\..*?%s)' % (re.escape(gs1), re.escape(gmk1)), br0, re.I|re.S)) or (re.search(r'(%s.*?\..*?%s)' % (re.escape(gmk1), re.escape(gs1)), br0, re.I|re.S)): #gs1 fullstop gmk1 and viceversa
            rg3.write(icc)
            rg3.write('\t')            
            rg3.write(file)
            rg3.write('\t')
            rg3.write(gs11)
            rg3.write('\t')
            rg3.write(br0)
            rg3.write('\t')
            rg3.write('Found %s in %s' % (gmk1, s1.strip())) # change to s1 
            rg3.write('\n')
    	
            
        if gmk1 == 'activation':
            if  re.search(r'(activation by %s)' %gs1, br0, re.I|re.S):
                ra1.write(icc)
                ra1.write('\t')                
                ra1.write(file)
                ra1.write('\t')
                ra1.write(gs11)
                ra1.write('\t')
                ra1.write(br0)
                ra1.write('\t')
                ra1.write('Found %s in %s' % (gmk1,s1.strip()))
                ra1.write('\n')
            if  re.search(r'(probably.*?%s activation)' %gs1, br, re.I|re.S|re.DOTALL):
                ra2.write(icc)
                ra2.write('\t')    
                ra2.write(file)
                ra2.write('\t')
                ra2.write(gs11)
                ra2.write('\t')
                ra2.write(br0)
                ra2.write('\t')
                ra2.write('Found %s in %s' % (gmk1,s1.strip()))
                ra2.write('\n')
            if  re.search(r'(critical for.*?%s activation)' %gs1, br, re.I|re.S):
                ra3.write(icc)
                ra3.write('\t')                
                ra3.write(file)
                ra3.write('\t')
                ra3.write(gs11)
                ra3.write('\t')
                ra3.write(br0)
                ra3.write('\t')
                ra3.write('Found %s in %s' % (gmk1,s1.strip()))
                ra3.write('\n') 
            if  re.search(r'(%s.*?activation of)' %gs1, br3, re.I|re.S):
                ra4.write(icc)
                ra4.write('\t')                
                ra4.write(file)
                ra4.write('\t')
                ra4.write(gs11)
                ra4.write('\t')
                ra4.write(br0)
                ra4.write('\t')
                ra4.write('Found %s in %s' % (gmk1,s1.strip()))
                ra4.write('\n')
        if gmk1 == 'deficient':

            if  re.search(r'(%s deficient)' %gs1, br0, re.I|re.S):
                rd1.write(icc)
                rd1.write('\t')
                rd1.write(file)
                rd1.write('\t')
                rd1.write(gs11)
                rd1.write('\t')
                rd1.write(br0)
                rd1.write('\t')
                rd1.write('Found %s in %s' % (gmk1, br))
                rd1.write('\n')
            if  re.search(r'(deficient.+?exhibited.+?%s)' %gs1, br0, re.I|re.S|re.DOTALL):
                rd2.write(icc)
                rd2.write('\t')
                rd2.write(file)
                rd2.write('\t')
                rd2.write(gs11)
                rd2.write('\t')
                rd2.write(br0)
                rd2.write('\t')
                rd2.write('Found %s in %s' % (gmk1,br))
                rd2.write('\n')
                
        if gmk1 == '-/-':
        
            if  re.search(r'(-/-%s)' %gs1, br0, re.I|re.S):
                rs1.write(icc)
                rs1.write('\t')
                rs1.write(file)
                rs1.write('\t')
                rs1.write(gs11)
                rs1.write('\t')
                rs1.write(br0)
                rs1.write('\t')
                rs1.write('Found %s in %s' % (gmk1,s1.strip()))
                rs1.write('\n')
            if  re.search(r'(%s-/-)' %gs1, br0, re.I|re.S):
                rs2.write(icc)
                rs2.write('\t')
                rs2.write(file)
                rs2.write('\t')
                rs2.write(gs11)
                rs2.write('\t')
                rs2.write(br0)
                rs2.write('\t')
                rs2.write('Found %s in %s' % (gmk1,s1.strip()))
                rs2.write('\n')      
        if gmk1 == '+':
            if  re.search(r'(%s+)' %gs1, br0, re.I|re.S):
                rs3.write(icc)
                rs3.write('\t')
                rs3.write(file)
                rs3.write('\t')
                rs3.write(gs11)
                rs3.write('\t')
                rs3.write(br0)
                rs3.write('\t')
                rs3.write('Found %s in %s' % (gmk1,s1.strip()))
                rs3.write('\n')
            if  re.search(r'(%s\(\+\))' %gs1, br3, re.I|re.S):
                rs5.write(icc)
                rs5.write('\t')
                rs5.write(file)
                rs5.write('\t')
                rs5.write(gs11)
                rs5.write('\t')
                rs5.write(br0)
                rs5.write('\t')
                rs5.write('Found %s in %s' % (gmk1,s1.strip()))
                rs5.write('\n')   
            else:
                rs6.write(icc)
                rs6.write('\t')
                rs6.write(file)
                rs6.write('\t')
                rs6.write(gs11)
                rs6.write('\t')
                rs6.write(br0)
                rs6.write('\t')
                rs6.write('Found %s in %s' % (gmk1,s1.strip()))
                rs6.write('\n')
        if gmk1 == 'induced':
            if  re.search(r'(%s.*?was shown.+?induced)' %gs1, br0, re.I|re.S|re.DOTALL):
                ri1.write(icc)
                ri1.write('\t')
                ri1.write(file)
                ri1.write('\t')
                ri1.write(gs11)
                ri1.write('\t')
                ri1.write(br0)
                ri1.write('\t')
                ri1.write('Found %s in %s' % (gmk1,s1.strip()))
                ri1.write('\n')
            if  re.search(r'(%s.*?-induced)' %gs1, br0, re.I|re.S):
                ri2.write(icc)
                ri2.write('\t')
                ri2.write(file)
                ri2.write('\t')
                ri2.write(gs11)
                ri2.write('\t')
                ri2.write(br0)
                ri2.write('\t')
                ri2.write('Found %s in %s' % (gmk1,s1.strip()))
                ri2.write('\n')
            if  re.search(r'(induced.*?to %s)' %gs1, br0, re.I|re.S):
                ri3.write(icc)
                ri3.write('\t')
                ri3.write(file)
                ri3.write('\t')
                ri3.write(gs11)
                ri3.write('\t')
                ri3.write(br0)
                ri3.write('\t')
                ri3.write('Found %s in %s' % (gmk1,s1.strip()))
                ri3.write('\n') 
            if  re.search(r'(induced.*?while %s)' %gs1, br0, re.I|re.S):
                ri4.write(icc)
                ri4.write('\t')
                ri4.write(file)
                ri4.write('\t')
                ri4.write(gs11)
                ri4.write('\t')
                ri4.write(br0)
                ri4.write('\t')
                ri4.write('Found %s in %s' % (gmk1,s1.strip()))
                ri4.write('\n')
        if gmk1 == 'inhibition':
            if  re.search(r'(hypothesized\s.*?\sinhibition\s.*?\s%s )' %gs1, br, re.I|re.S):
                rin1.write(icc)
                rin1.write('\t')
                rin1.write(file)
                rin1.write('\t')
                rin1.write(gs11)
                rin1.write('\t')
                rin1.write(br0)
                rin1.write('\t')
                rin1.write('Found %s in %s' % (gmk1,s1.strip()))
                rin1.write('\n')
        if gmk1 == 'knockout':
            if  re.search(r'(effect of %s knockout)' %gs1, br3, re.I|re.S):
                rk1.write(icc)
                rk1.write('\t')
                rk1.write(file)
                rk1.write('\t')
                rk1.write(gs11)
                rk1.write('\t')
                rk1.write(br0)
                rk1.write('\t')
                rk1.write('Found %s in %s' % (gmk1,s1.strip()))
                rk1.write('\n')
            if  re.search(r'(double knockout)', br3, re.I|re.S): # for the time being
                rk2.write(icc)
                rk2.write('\t')
                rk2.write(file)
                rk2.write('\t')
                rk2.write(gs11)
                rk2.write('\t')
                rk2.write(br0)
                rk2.write('\t')
                rk2.write('Found %s in %s' % (gmk1,s1.strip()))
                rk2.write('\n')
        if gmk1 == 'KO':
            if  re.search(r'(double KO\W)', br3, re.I|re.S): # for the time being
                rko1.write(icc)
                rko1.write('\t')
                rko1.write(file)
                rko1.write('\t')
                rko1.write(gs11)
                rko1.write('\t')
                rko1.write(br0)
                rko1.write('\t')
                rko1.write('Found %s in %s' % (gmk1,s1.strip()))
                rko1.write('\n')                
                
        if gmk1 == 'mutant':
            if  re.search(r'(harboring.*?%s mutant)' %gs1, br, re.I|re.S):
                rm1.write(icc)
                rm1.write('\t')
                rm1.write(file)
                rm1.write('\t')
                rm1.write(gs11)
                rm1.write('\t')
                rm1.write(br0)
                rm1.write('\t')
                rm1.write('Found %s in %s' % (gmk1,s1.strip()))
                rm1.write('\n')
            if  re.search(r'(mutant.*?causes.*?%s)' %gs1, br0, re.I|re.S):
                rm2.write(icc)
                rm2.write('\t')
                rm2.write(file)
                rm2.write('\t')
                rm2.write(gs11)
                rm2.write('\t')
                rm2.write(br0)
                rm2.write('\t')
                rm2.write('Found %s in %s' % (gmk1,s1.strip()))
                rm2.write('\n')
                
        if gmk1 == 'stimulated':
            if  re.search(r'(.*?-stimulated.*?%s)' %gs1, br, re.I|re.S):
                rst2.write(icc)
                rst2.write('\t')
                rst2.write(file)
                rst2.write('\t')
                rst2.write(gs11)
                rst2.write('\t')
                rst2.write(br0)
                rst2.write('\t')
                rst2.write('Found %s in %s' % (gmk1,s1.strip()))
                rst2.write('\n')
            if  re.search(r'(%s-stimulated)' %gs1, br0, re.I|re.S):
                rst1.write(icc)
                rst1.write('\t')
                rst1.write(file)
                rst1.write('\t')
                rst1.write(gs11)
                rst1.write('\t')
                rst1.write(br0)
                rst1.write('\t')
                rst1.write('Found %s in %s' % (gmk1,s1.strip()))
                rst1.write('\n')
        if gmk1 == 'treated':
            
            if  re.search(r'(control or %s-treated)' %gs1, br3, re.I|re.S):
                rt2.write(icc)
                rt2.write('\t')
                rt2.write(file)
                rt2.write('\t')
                rt2.write(gs11)
                rt2.write('\t')
                rt2.write(br0)
                rt2.write('\t')
                rt2.write('Found %s in %s' % (gmk1,s1.strip()))
                rt2.write('\n')
 
    return 4        
              


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
    #rt1.close()
    rt2.close() 
    rs4.close()
    rs5.close()
    rs6.close() 
    #rrr.close()
            

    
c=0
for path, dirs, files in os.walk(r'L:\My Online Documents\MTech\series_imp_info'):
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
            #if s.startswith('!Series_title') or s.startswith('!Series_summary') or s.startswith('!Series_overall_design'):
            if s.startswith('!series_title') or s.startswith('!series_summary') or s.startswith('!series_overall_design'):    
                for gmk in a:
                    gmk = gmk.rstrip() #to remove the lagging \n in many GMKs
                    gmk = gmk.lower()
                    find_matches(s, gmk)
closef()
print("--- %s seconds ---" % (time.time() - start_time))
      
          
    
