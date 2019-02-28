# https://codeforces.com/contest/727/problem/A

#coding: utf-8

a, b = map(int, raw_input().split())

numbers = []
numbers.append(b)

while (b > a):
	aux = str(b)
	
	if (int(aux[-1]) == 1):
		b = (b-1)/10
		numbers.append(b)
	elif ((int(aux[-1]) % 2) == 0):
		b = (b/2)
		numbers.append(b)
	else:
		break
	
	
result = ""

if (b == a):
	print "YES"
	print len(numbers)
	
	for i in range(len(numbers)-1, -1, -1):
		if (i == 0):
			result += str(numbers[i])
		else:
			result += str(numbers[i]) + " "			
		
	print result
else:
	print "NO"
