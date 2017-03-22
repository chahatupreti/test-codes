# import numpy
a=open(r'C:\Users\Krishna\Desktop\ALL\up down analysis for orgs\here_we file matches_mouse.txt').readlines()
b=open(r'C:\Users\Krishna\Desktop\ALL\up down analysis for orgs\files done so far_actual.txt').readlines()
# q=[]
# for a1 in a:
# 	a1=a1.rstrip()
# 	q.append(a1)
# # print(q)
# q1=[]
# for a1 in b:
# 	a1=a1.rstrip()
# 	q1.append(a1)
# print(q)
a=[a1.rstrip() for a1 in a]
b=[b1.rstrip() for b1 in b]
# print (a)
c=[item for item in a if item not in b]
# c=[item for item in q]
[print(c1) for c1 in c]