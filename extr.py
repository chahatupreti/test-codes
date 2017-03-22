v=0
f=[]
e=open(r'D:\M.Tech work\test codes\nbnn.txt','w')
dd=open(r'F:\M.Tech\for assigning cl\ruless occurence\gmks start7.txt').readlines()
for d in dd: 
	d=d.rstrip()
	if (d.startswith('GSE') or d.startswith('Found')):
		f.append(d)
for i in xrange(len(f)):
	if f[i].startswith('Found'):
		f[i]=f[i][0:70]
for d in f:
	e.write(d)
	e.write('\n')
e.close()

# a=open(r'D:\M.Tech work\test codes\r500 hfgm not passed1.txt').readlines()
# for b in a:
# 	if b.startswith('the GS modified') or b.startswith('GSE'):
# 		print b