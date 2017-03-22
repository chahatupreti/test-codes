a=open(r'C:\Users\Krishna\Desktop\ALL\up down analysis for orgs\here_we file match with GS.txt').readlines()
b=open(r'C:\Users\Krishna\Desktop\ALL\up down analysis for orgs\50 files for here we.txt', 'r').readlines()
# with open(r'C:\Users\Krishna\Desktop\ALL\up down analysis for orgs\effect_on file matches_mouse.txt', encoding='utf-8') as b:
	# mb=b.readlines()
mb=b
# b=b.replace('\n', '')
# print(mb)
# for b1 in b:
# 	b1 = b1.rstrip('\n')
# 	print (b1)

for i,e in enumerate(mb):
	mb[i] = mb[i].rstrip('\n')
	# print (b1)

# print(b)
for aa in a:
	aaa = aa.split()
	# print (aaa)
	# print (b)
	if aaa[0] in mb:
		# None
		print (aa)