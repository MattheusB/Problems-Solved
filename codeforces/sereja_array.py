# https://codeforces.com/contest/315/problem/B

#coding: utf-8

entrance = raw_input().split()

n = int(entrance[0])
m = int(entrance[1])

array = map(int, raw_input().split())

aux = 0

for i in range(m):
    operations = map(int, raw_input().split())
    if(operations[0] == 1):
        array[operations[1]- 1] = operations[2] - aux
	
	
    elif(operations[0] == 2):
            aux += operations[1]
			
    else:
        print array[operations[1]-1] + aux
