# https://codeforces.com/contest/750/problem/B

#coding: utf-8

n = int(raw_input())
cont = 0
answer = True

for i in range(n):
	coordinate, direction = raw_input().split()
	coordinate = int(coordinate)
	
	if (direction == "South"):
		cont += coordinate
		
	elif (direction == "North"):
		cont -= coordinate
		
	elif (cont == 0 or cont == 20000):
		answer = False		
		
	if (cont < 0 or cont > 20000):
		answer = False
		
if (answer == True and cont == 0):
	print "YES"
else:
	print "NO"
