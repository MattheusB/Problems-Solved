# https://codeforces.com/contest/339/problem/B

#coding: utf-8


n, m = map(int,raw_input().split())
array = map(int,raw_input().split())
answer = 0 ; aux1 = 1
for i in range(m):
    aux2 = array[i]
    if (aux2 > aux1): 
    	answer += aux2 - aux1
    	aux1 = aux2
    elif (aux1 > aux2): 
    	answer += n - aux1 + aux2 
    	aux1 = aux2
print answer
