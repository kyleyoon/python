#!/usr/bin/env python

print "Hello WMP"

p = 1000
rate = 0.05
numyears = 5
year = 1
while year <= numyears:
    a = p * (1 + rate)
    year = year + 1
    print year, a, p

print "%3d %0.2f" % (12122141, 12412104120)
print format(12122141,"3d"), format(12412104120,"0.2f")
print "{0:3d} {1:0.2f}".format(12122141,12412104120)

print 'c', 'd'

