# import cProfile, pstats, StringIO
# pr = cProfile.Profile()
# pr.enable()
import shutil
import os
import re
import time
#from rules1_no_print import cl
start_time = time.time()
#q=open('C:\Users\Krishna\Desktop\up down analysis for orgs\checking rules.txt','w')
a = open('F:\M.Tech\patterns for gmk_down.txt','r').readlines()
a1 = open('F:\M.Tech\patterns for gmk_up.txt','r').readlines()
a=a+a1


#rr1 = open(r'F:\M.Tech\for assigning cl\test\gmks start7.txt', 'w')
#ro11 = open(r'F:\M.Tech\for assigning cl\rules occurence\s\overexpression one1.txt', 'w')

g=[]
c=0
for path, dirs, files in os.walk(r'F:\M.Tech\for assigning cl\selected\random 500'):
    for file in files:
        sentences = open(os.path.join(path,file),'r').readlines();
        c = c+1
        r=0
        rr=0
        rt=0
        
        #print c # one value printed for each file
        #print file
        #print("--- %s seconds ---" % (time.time() - start_time))
#        k=0
        hg=''
        for s in sentences:
            if s.startswith('!Sample_organism_ch1\t"Mus musculus"'):
                r=1
               
        if r==1:
            g.append(file)
        
        else:
            None
            #print 'NOT MOUSE'
print len(g)
# for c11 in g:
#     shutil.copy(r'F:\M.Tech\for assigning cl\selected\random 500_l\\'+c11,r'F:\M.Tech\for assigning cl\selected\mouse in random 500_l\\'+c11)
print("--- %s seconds ---" % (time.time() - start_time))   
   
#pr.disable()
#s = StringIO.StringIO()
#sortby = 'cumulative'
#ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
#ps.print_stats()
#print s.getvalue()
