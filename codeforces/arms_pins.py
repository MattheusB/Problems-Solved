# https://codeforces.com/contest/507/problem/B

#coding: utf-8
from math import ceil, sqrt


r, x, y, x1, y1 = map(int, raw_input().split())

if ((x == x1) and (y == y1)):
	print 0
else:
	a = (x1 - x)**2
	b = (y1 - y)**2
	w = (sqrt(a+b))/(r*2)
	v = int(ceil(w))
	print v
