#!/usr/bin/python

import sys

l = sys.stdin.readline().strip().split()
x = int(sys.stdin.readline().strip())
l = [int(i) for i in l]
l = sorted(l)

def binary_search(l, x):
	print l
	med = l[int(len(l) / 2.)]
	if x == med:
		print 'equal'
		return
	if x == med or len(l) == 1:
		print 'found x'
		#print med
		return 

	if x > med:
		binary_search(l[int(len(l)/2.):], x)

	if x < med:
		binary_search(l[:int(len(l)/2)], x)


binary_search(l, x)
