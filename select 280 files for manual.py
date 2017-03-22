import os
import shutil
a=''
w2=''
w=open(r'F:\M.Tech\for assigning cl\for samples.txt','r').readlines()
#print w[0]
#we=[we.rstrip(r'\n') for we in w]
we=[we.rstrip('\n') for we in w]
##for ww in w:
##    print ww
##    ww=ww.rstrip('\n')
##    print ww
##ww=[]
print we
w = [x.rstrip('\n') for x in w]
print w
##for path, dirs, files in os.walk(r'F:\M.Tech\for assigning cl\series_imp_info'):
##    for file in files:
##        a = file
##        for w1 in w:
##            w2='GSE'+w1+'_series_matrix.txtimp_info.txt'
##        #b=a[0:-1]
##        #print b[5:7]
##            if (w2==file):
##                print 45
##                shutil.copy(r'F:\M.Tech\for assigning cl\series_imp_info\\'+a,r'F:\M.Tech\for assigning cl\selected\\'+a)
            
