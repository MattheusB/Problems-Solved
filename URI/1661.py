# https://www.urionlinejudge.com.br/judge/pt/problems/view/1661

#coding: utf-8

n = int(raw_input())

while n != 0:



	a = map(int, raw_input().split())

	aux = []
	
	for i in range(len(a)):
		aux.append(a[i])

	answer = 0
	
	for i in range(1, len(aux)):
		if aux[i-1] < 0:
			answer = answer + (-1 * aux[i-1])
		else:
			answer = answer + aux[i-1]
		aux[i] = aux[i] + aux[i-1]
			
	print answer		
	n = int(raw_input())


