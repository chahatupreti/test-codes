# a=open(r'F:\M.Tech\mouse_gs_small_simple.txt','r').readlines()
# b=open(r'F:\M.Tech\mouse_gs_small_simple_reduced.txt','r').readlines()
# c=open(r'C:\Users\Krishna\Desktop\up down analysis for orgs\removed gs.txt','w')
# #d=[]
# d= [item for item in a if item not in b]
# 	#print ite
# for dd in d:
# 	c.write(dd)

# c.close()

a=open(r'F:\M.Tech\mus musculus_other_designation_only1.txt','r').readlines()
b=open(r'F:\M.Tech\mus musculus_other_designation_only.txt','r').readlines()
#c=open(r'C:\Users\Krishna\Desktop\up down analysis for orgs\removed gs.txt','w')
#d=[]
d= [item for item in a if item not in b]
	#print ite
for dd in d:
	print dd

#c.close()
