import sys
ch=0
w=0
x=0
xx=[]
t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    ch=int(n/c)
    w=ch
    x=ch
    while w>=m:
        ch=int(w/m)
        x=x+ch
        cr=w%m
        w=ch+cr
    xx.append(x)
for i in xrange(t):
    print xx[i]