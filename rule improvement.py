# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:01:16 2016

@author: Krishna
"""
import re

def cl(s, gmk, gs, data):
    s=s.replace(gs, '_8MILLION8_')
    gs='_8MILLION8_'
    #l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|"|\'|[()]|-', s)
    l = s.split() 
    for ii in range(0,len(data)):
        print 'loop'
        a = data[ii]
        lo = min(a[1], a[2])
        hi = max(a[1], a[2])
        br = l[max(0, lo-8):hi+8]
        br= " ".join(br)
        beg_gmk = ['over-activation', 'overexpression', 'loss of', 'knockout', 'haplo-insuffiency', 'haploinsufficiency', 'inactivation', 'knock-out', 'deletion', 'inhibition', 'knockdown', 'silencing']
        beg_other = ['Global gene expression', 'Gene expression profiling', 'Expression data', 'Gene expression analysis']
        for i in range(0,len(beg_gmk)):
            if re.search(r'(^!Series_.*?\s"%s)' %beg_gmk[i], s, re.I|re.S):   # this rule looks optimum
                print 1
        for i in range(0,len(beg_other)):
            if re.search(r'(^!Series_.*?\s"%s)' %beg_other[i], s, re.I|re.S):  # this rule looks optimum 
                print 2
        if re.search(r'(^!Series_\w.*?\s"Keywords:)', s):
            ll=s.split(',')
            v=0
            for i in range(0,len(ll)):
                if gmk and gs in ll[i]:
                    print 222
                    v=4                          # this rule is now optimum   
            if v!=4:
                print 233
            
            #if re.search(r'(%s.*?,.*?%s)' % (re.escape(gs), re.escape(gmk)), s, re.I|re.S) or (re.search(r'(%s.*?,.*?%s)' % (re.escape(gmk), re.escape(gs)), s, re.I|re.S)): 
                print 3
        
        br0 = l[max(0, lo):hi]  # we dont need the 8 words here and there as the fullstop is between gmk and gs
        br0=' '.join(br0)
        print br0
        if (re.search(r'(%s.*?\.\s.*?%s)' % (re.escape(gs), re.escape(gmk)), br0, re.I|re.S)) or (re.search(r'(%s.*?\.\s.*?%s)' % (re.escape(gmk), re.escape(gs)), br0, re.I|re.S)): #gs fullstop gmk and viceversa
            print 4                                                        # this rule is now close to optimum
        
        
        br3 = l[max(0, lo-3):hi+3] 
        br3=' '.join(br3)
        if re.search(r'(%s\(control\))' %gs, br3, re.I|re.S): #gs(control)
            print 5
        
        if re.search(r'(The object of this study was to identify genes transcriptionally upregulated.*?downregulated)', s):
            print 6                  # not optimum but should be fast
            
            
        if gmk == 'activation':
            #if 'activation by %s' %gs in br0:
            if  re.search(r'(activation by %s)' %gs, br0, re.I|re.S):
                print 7 
                
            if  re.search(r'(probably\s.*?\s %s activation)' %gs, br, re.I|re.S):
                print 8
            if  re.search(r'(critical for.*?%s activation)' %gs, br, re.I|re.S):
                print 9 
            if  re.search(r'(%s.*?activation of)' %gs, br3, re.I|re.S):
                print 10
        if gmk == 'deficient':
            if  re.search(r'(%s deficient)' %gs, br0, re.I|re.S):
                print 11
            if  re.search(r'(deficient\s.*?\sexhibited\s.*?\s%s)' %gs, br0, re.I|re.S):
                print 12
        #    if gmk == 'deletion':
        #        for all_gs in keywords:
                #all_gs=all_gs.rstrip()
        #            if re.search(r'(\s%s-deletion\s.*?\s%s)' % (re.escape(all_gs), re.escape(gs)), s, re.I|re.S):
        #                print 13       
        if gmk == '-/-':
           # if data[ii][0]<3:     # optimum now
           #     print 14
            if  re.search(r'(-/-%s)' %gs, br0, re.I|re.S):
                print 15
            if  re.search(r'(%s-/-)' %gs, br0, re.I|re.S):
                print 16      
        if gmk == '+':
            if  re.search(r'(%s+)' %gs, br0, re.I|re.S):
                print 17
            elif  re.search(r'(%s\(\+\))' %gs, br3, re.I|re.S):
                print 18   
            else:
                print 19
        if gmk == 'induced':
            if  re.search(r'(%s.*?was shown\s.*?\sinduced)' %gs, br0, re.I|re.S):
                print 20
            if  re.search(r'(%s.*?-induced)' %gs, br0, re.I|re.S):
                print 21
            if  re.search(r'(induced.*?to %s)' %gs, br0, re.I|re.S):
                print 22 
            if  re.search(r'(induced.*?while %s)' %gs, br0, re.I|re.S):
                print 23
        if gmk == 'inhibition':
            if  re.search(r'(hypothesized\s.*?\sinhibition\s.*?\s%s )' %gs, br, re.I|re.S):
                print 24
        if gmk == 'knockout':
            if  re.search(r'(effect of %s knockout)' %gs, br3, re.I|re.S):
                print 25
            if  re.search(r'(double knockout)', br3, re.I|re.S): # for the time being
                print 26
        if gmk == 'KO':
            if  re.search(r'(double KO\W)', br3, re.I|re.S): # for the time being
                print 27
        if gmk == 'mutant':
            if  re.search(r'(harboring.*?%s mutant)' %gs, br3, re.I|re.S):
                print 28
            if  re.search(r'(mutant.*?causes.*?%s)' %gs, br0, re.I|re.S):
                print 29
        #    if gmk == 'null':
        #        for all_gs in keywords:
                #all_gs=all_gs.rstrip()
        #            if re.search(r'(matched %s\s.*?\s%s.*?null)' % (re.escape(gs), re.escape(all_gs)), s, re.I|re.S): #doing %gs, %all_gs gave syntax error. THIS NEW WAY IS THE RIGHT WAY TO DO IT
        #                print 30
        if gmk == 'stimulated':
            if  re.search(r'(.*?-stimulated.*?%s)' %gs, br, re.I|re.S):
                print 31
            if  re.search(r'(%s-stimulated)' %gs, br0, re.I|re.S):
                print 32
        if gmk == 'treated':
            if  re.search(r'(treated.*?control.*?%s)' %gs, br0, re.I|re.S):
                print 33
            if  re.search(r'(control or %s-treated)' %gs, br3, re.I|re.S):
                print 34
    return 4        
          
s='!Series_title	"aquaporin protein-1 the flory,, of gthys loss of in this proffession by in aquaporin protein-1 its loss of b , aquaporin protein-1"'

gs = 'aquaporin protein-1'
# i have s, gmk, gs, data
gmk = 'loss of'      
k1 = "_KEYWORD_1_"
k2 = "_KEYWORD_2_"
s1 = s.replace(gmk, k1)
s1 = s1.replace(gs, k2)

lt = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|"|\'|[()]|-', s1)
lt=filter(None, lt)
print lt
d_idx = {k1:[], k2:[]}
#print d_idx[k1]
for k,v in enumerate(lt):
    #print k,v
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
print data
r=cl(s1, gmk, gs, data)
print r
  


#if (re.search(r'(%s.*?\..*?%s)' % (re.escape(gs), re.escape(gmk)), s, re.I|re.S)) or (re.search(r'(%s.*?\..*?%s)' % (re.escape(gmk), re.escape(gs)), s, re.I|re.S)): #gs fullstop gmk and viceversa
#        print 4
