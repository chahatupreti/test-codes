import os
import itertools
a=open(r'C:\Users\Krishna\Desktop\up down analysis for orgs\files used in 14k.txt','w')
for path, dirs, files in os.walk(r'L:\My Online Documents\MTech\rules occurence\seg\one'):
    for file in files:
        f1 = open(os.path.join(path,file),'r')
        fif = itertools.islice(f1, 0, None, 6)
        for line in fif:
        	a.write(line)
        f1.close()

for path, dirs, files in os.walk(r'L:\My Online Documents\MTech\rules occurence\seg\two'):
    for file in files:
        f1 = open(os.path.join(path,file),'r')
        fif = itertools.islice(f1, 0, None, 3)
        for line in fif:
        	a.write(line)
        f1.close()

for path, dirs, files in os.walk(r'L:\My Online Documents\MTech\rules occurence\seg\three'):
    for file in files:
        f1 = open(os.path.join(path,file),'r')
        fif = itertools.islice(f1, 0, None, 4)
        for line in fif:
        	a.write(line)
        f1.close()
a.close()
        