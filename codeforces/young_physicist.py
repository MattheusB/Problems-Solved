# https://codeforces.com/contest/69/problem/A

#coding: utf-8
m = int(raw_input())

soma = 0
x = 0
y = 0
z = 0


for i in range(m):
   	coordinates = raw_input().split(" ")
	x += int(coordinates[0])
	y += int(coordinates[1])
	z += int(coordinates[2])
	
if (x == 0 and y == 0 and z == 0):
    print "YES"
else:
    print "NO"
