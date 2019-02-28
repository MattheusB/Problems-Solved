# https://codeforces.com/contest/520/problem/B

#coding: utf-8

n, m = map(int, raw_input().split())

cont = 0

if (n > m):
	print n - m
	
else:
	while (m > n):
		if (m % 2 != 0):
			cont += 1
			m += 1
		m = m/2
		cont += 1
		
	cont += n -m
	
	print cont
