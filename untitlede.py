# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 12:55:53 2016

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


ra3 = open(r'L:\My Online Documents\MTech\ruless occurence\activation three.txt', 'w')



keyword1 = open('F:\M.Tech\mouse_gs_small_simple_reduced.txt','r').readlines()  # this has the new small GS
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
                        
                      
                    if data: 
                        cl(s, gmk, gs, gs_list, data)
                        
def cl(s1, gmk1, gs1, gs_list1, data1): # output will be the confidence level    
    #print("CL--- %s seconds ---" % (time.time() - start_time))
    #print 'something'    
    #print  'gmk1 is %s' %gmk1
    #print  'gs1 is %s' %gs1    
    gs11=gs1 # saving the GS to display in the final file
    br0=''
    br3=''
    br=''
    gs_list1.remove(gs1) # AS WE WANT TO USE THIS LIST FOR GETTING THE GS'S THAT ARE APART FROM THE CURRENT GS        
    s1 = re.sub(r'(\b(%s)\b)' % (gs1), r'_8MILLION8_', s1, flags=re.I) # inserts the token wherever there is GS. The \b before & after ensures this doesnt happen in between words

    #s1=s1.replace(gs1, '_8MILLION8_')
    gs1='_8MILLION8_'
    #l = re.split('\s|(?<!\d)[,.]|[,.](?!\d)|;|"|\'|[()]|-', s)  KEEP THIS AS AN ARCHIVE
    l = s1.split()  # i switched from the complex split above to just space split to ensure that the splitters can be part of a rule
    
   
    
    
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

#        if gmk1 == 'deletion':
#   
#            for all_gs in gs_list1:
#             
#                if re.search(r'(%s-deletion.*?%s)' % (re.escape(all_gs), re.escape(gs1)), br3, re.I|re.S):
#                
#                    rde1.write(file)
#                    rde1.write('\n')
#                    rde1.write(gs11)
#                    rde1.write('\n')
#                    rde1.write('Found %s in: %s' % (gmk1,br)) #change to s1.strip() later
#                    rde1.write('\n')  
#                   
#       
#        if gmk1 == 'null':
#            for all_gs in gs_list1:
#           
#                if re.search(r'(%s.*?%s.*?null)' % (re.escape(gs1), re.escape(all_gs)), br3, re.I|re.S): #doing %gs, %all_gs gave syntax error. THIS NEW WAY IS THE RIGHT WAY TO DO IT
#                    
#                    rn1.write(file) 
#                    rn1.write('\n')
#                    rn1.write(gs11)
#                    rn1.write('\n')
#                    rn1.write('Found %s in: %s' % (gmk1,br3)) #change to s1.strip() later
#                    rn1.write('\n')
                    
   
            
        if gmk1 == 'activation':
           
            if  re.search(r'(critical for.*?%s activation)' %gs1, br, re.I|re.S):
                ra3.write(file)
                ra3.write('\n')
                ra3.write(gs11)
                ra3.write('\n')
                ra3.write(br)
                ra3.write('\n')
                ra3.write('Found %s in %s' % (gmk1,s1.strip()))
                ra3.write('\n') 
          
    return 4        


def closef():
    
    ra3.close()
    
    
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
      
          
    
