import re
import os
a=[]
for path, dirs, files in os.walk(r'E:\F DRIVE\M.Tech\for assigning cl\mouse in series_ll'):
	for file in files:
		h=file.split('_')
		j=h[0]
		jj=j.split('-')
		j1=jj[0]
		a.append(j1)

aa=open(r'E:\F DRIVE\M.Tech\for assigning cl\etc\mouse files.txt','w')
for i in range(len(a)):
	aa.write(a[i])
	aa.write('\n')

b=open(r'E:\F DRIVE\M.Tech\for assigning cl\new_improved_rules\testing creed data\filenames with mouse in first half.txt').readlines()
for i in range(len(b)):
	b[i]=b[i].rstrip()
print (list(set(a).intersection(b)))
c=list(set(a) & set(b))

for cc in c:	print (cc)
aa.close()