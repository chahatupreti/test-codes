#a=[1,2,3,4,5]
#b=[7,5,7,8,3,2]
#c=[43,45,76,3,5]
#e=[[] for x in xrange(3)]
#e[0]=a
#e[1]=b
#e[2]=c
#
#for i in range(0,len(e)):
#    print e[i]
#    print 'er'
#    

import numpy
#list1=[1,2,3]
#list2=[4,5,6]
#a=numpy.array(list1)
#b=numpy.array(list2)
#c=a+b
#print c

import matplotlib.pylab as plt
#plt.ion()
#plt.plot([1,2,3])
#plt.show()
#plt.ylabel('This is an axis')
#print ("Hello")

from mpl_toolkits.mplot3d import Axes3D

# Set up grid and test data
nx, ny = 256, 1024
x = range(nx)
y = range(ny)

data = numpy.random.random((nx, ny))

hf = plt.figure()
ha = hf.add_subplot(111, projection='3d')

X, Y = numpy.meshgrid(y, x)  # `plot_surface` expects `x` and `y` data to be 2D
ha.plot_surface(X, Y, data)

plt.draw()