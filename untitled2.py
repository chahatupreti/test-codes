import re
d = 'the flory of gthys inhibition in this proffession by in aquaporin protein-1  its inhibition by the state of the art in aquaporin 2'
a = 'aquaporin protein-1'
b = 'inhibition'
diff=500
l = re.split(';|,|-| ', d)
l1 = re.split(';|,|-| ', a)
l2 = re.split(';|,|-| ', b)
counts=[m.start() for m in re.finditer(a, d)]
counts1=[m.start() for m in re.finditer(b, d)]
for cc in counts:
    for c1 in counts1:
        if abs(cc-c1) < diff:
            diff = abs(cc-c1)
            values = (cc, c1)



if d.find(a) < d.find(b):
    r= (l.index(l2[0]) - l.index(l1[-1]))
if d.find(a) > d.find(b):
    r= (l.index(l1[0]) - l.index(l2[-1]))
if r<6:
    print 'matched'
    print r


    
