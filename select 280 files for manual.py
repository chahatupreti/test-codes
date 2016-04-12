import os
import shutil
a=''
b=[]
for path, dirs, files in os.walk(r'L:\My Online Documents\MTech\series_imp_info'):
    for file in files:
        a = file
        b=a[0:-1]
        #print b[5:7]
        if (b[6:8]=='25') or (b[6:8]=='75'):
            print 45
            shutil.copy(r'L:\My Online Documents\MTech\series_imp_info\\'+a,r'L:\My Online Documents\MTech\selected\s1\\'+a)
            