# https://codeforces.com/contest/455/problem/A

#coding: utf-8

max_n = 100001

array1= [0]*max_n
array2 = [0]*max_n

n = int(raw_input())
sequence = map(int, raw_input().split())
for i in xrange(0, n):
	array2[sequence[i]] += 1
array1[0] = 0
array1[1] = array2[1]

for j in xrange(2, max_n):
	array1[j] = max((array1[j-1]), (array1[j-2] + (j*array2[j])))
print array1[max_n-1]
