d={'A':['B','c','d'], 'X':['w','Q','z','y']}

f=['a','aa']
ff=['b','xx']
# {k.lower():v.lower()
#     for k, v in
#     d.iteritems()
# }
# outdict = {}
# for k, v in d.items():
#     outdict[k.lower()] = v.lower()
# s={k.lower(): v for k, v in d.items()}
# print(s)
import ast
dd=ast.literal_eval(str(d).lower())
print (dd)
# outdict1 = {}
# for k, v in {'My Key': 'My Value'}.items():
#     outdict1[k.lower()] = v.lower()
# print (outdict1)
# for i in range(len(d)):
# 	print (d)
kk=''
for i in range(len(f)):
	if f[i] in d.keys():
		print (12)
		print (f[i])
		kk=f[i]
		if ff[i] in d[kk]:
			print(34)