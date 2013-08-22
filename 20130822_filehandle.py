#! /usr/bin/env python

year = 1
numyears = 5
test = 1000
rate = 0.1

f = open("test","w")
while year <= numyears:
    test = test * (1+rate)
    print >>f,"%3d %0.2f" % (year,test)
    year += 1
f.close()

f = open("test")
line = f.readline()
 while line:
    print line
    line = f.readline()
    f.close()
ab = ['a','b',['c','d'],'e','f',['g','h',['i','j']]]
print ab[5][2][0]

s = set([1,2,3,4,5,5,6])
f = set([5,6,7,8,9,9,10])
ss = s | f
ff = s & f
kk = ss - ff
print kk

a = "a,bcdefg d"
for i in a:
  print i,
    
