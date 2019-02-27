# https://www.urionlinejudge.com.br/judge/pt/problems/view/1089

#coding: utf-8

n = int(raw_input())

while n != 0:
	waves = map(int, raw_input().split())
	up = True
	down = True
	peaks = 0
	
	aux = waves[0]
	

	for i in range(n):
		if (up == True and waves[i] < aux):
			down = True
			up = False
			peaks += 1
		elif (down == True and waves[i] > aux):
			down = False
			up = True
			peaks += 1

		aux = waves[i]

	if (up == True and waves[n-1] > waves[0]):
		peaks += 1
	elif(down == True and waves[n-1] < waves[0]):
		peaks += 1

	if (peaks % 2 == 0):
		print peaks
	else:
		print peaks -1

	n = int(raw_input())
