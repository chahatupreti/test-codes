# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 12:25:23 2015

@author: Krishna
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:20:10 2015

@author: Krishna
"""

import os
import re



#keywords = open('C:\Users\Krishna\Documents\ztestt.txt','r').readlines()
q=open('C:\Users\Krishna\Desktop\gmk_u1.txt','w')
keywords = open('F:\M.Tech\patterns for gmk_up.txt','r').readlines()  # this has the down keywords
c=0
for path, dirs, files in os.walk('D:\M.Tech work\test codes'):
    for file in files:

        sentences = open(os.path.join(path,file),'r').readlines();
        c = c+1
        r=0
        print c
        k=0
        for sentence in sentences:
            if k in (0,1,3): #to select only those 3 lines
                k=k+1
#                if r==1:
#                    break
                for keyword in keywords:
               #     print k, 'file ', c, 'line', r, file
                    #k=k+1
                    key2 = re.escape(keyword.rstrip())
                    if re.search(r'\b%s\b' % key2, sentence):
              #          print("Found '%s' in '%s'" % (keyword.strip(), sentence.strip()))
                        q.write(file)
                        q.write('\t')
                        q.write("Found '%s' in '%s'" % (keyword.strip(), sentence.strip()))
                        q.write('\n')
#                        r=1
#                        break
q.close()
                   
      
          
    
