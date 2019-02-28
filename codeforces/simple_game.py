# https://codeforces.com/contest/570/problem/B

#coding: utf-8

n, m = map(int, raw_input().split())
answer = 0

if (n == 1):
	answer = 1
elif (m > (n/2)):
	answer = m - 1
else:
	answer = m + 1
	
print answer
