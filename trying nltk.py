# -*- coding: utf-8 -*-
"""
Created on Tue May 03 14:50:10 2016

@author: Krishna
"""
#from collections import Counter
#a=['q','fd','fhj','dvd']
#b=['q','we','qw']
#a=Counter(a)
#b=Counter(b)
#a=list(a-b)
#print a
#for tt in a:
#    print tt

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

import matplotlib.pylab as pet
#plt.ion()
#plt.plot([1,2,3])
#plt.show()
#plt.ylabel('This is an axis')
#print ("Hello")

#from mpl_toolkits.mplot3d import Axes3D
#
## Set up grid and test data
#nx, ny = 256, 1024
#x = range(nx)
#y = range(ny)
#
#data = numpy.random.random((nx, ny))
#
#hf = plt.figure()
#ha = hf.add_subplot(111, projection='3d')
#
#X, Y = numpy.meshgrid(y, x)  # `plot_surface` expects `x` and `y` data to be 2D
#ha.plot_surface(X, Y, data)
#
#plt.draw()

#import nltk
#from nltk.book import *
#dcprint text5.plot
#text1.similar("day")

#print nltk.__path__

#print " ".join(text6[1:30])
#t=text5[16715:16735]

#print " ".join(t)


#sent = ['word1', 'word2', 'word3', 'word4', 'word5', 'word6', 'word7', 'word8', 'word9', 'word10']
#sent[0] = 'First'
#sent[9] = 'Last'
#len(sent)
#sent[1:9] = ['Second', 'Third']
#print sent
#print len(sent)

#saying = ['After', 'all', 'is', 'said', 'and', 'done', 'more', 'is', 'said', 'than', 'done']
#tokens = set(saying)
#tokens = sorted(tokens)
#print tokens[-2:]
#print text1

#print [len(w) for w in text1]
#print " ".join(w.upper() for w in text5)



#from mpl_toolkits.mplot3d import Axes3D

# Set up grid and test data
nx, ny = 256, 1024
x = range(nx)
y = range(ny)

data = numpy.random.random((nx, ny))

hf = pet.figure()
ha = hf.add_subplot(111, projection='3d')

X, Y = numpy.meshgrid(y, x)  # `plot_surface` expects `x` and `y` data to be 2D
ha.plot_surface(X, Y, data)

pet.draw()

#print len(set(word.lower() for word in text1 if word.isalpha()))
#print len(set(word for word in text1 if word.islower()))
#nltk.chat.chatbots()
#def f(): raise Exception("Found exit()")

#a=[0.4,0.064]
#a=sorted(a)
#print a
     









