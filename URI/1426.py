# https://www.urionlinejudge.com.br/judge/pt/problems/view/1426

#coding: utf-8

N = int(raw_input())

for i in range(N):
	first = map(int, raw_input().split())
	second = [0,0]
	third = map(int, raw_input().split())
	fourth = [0,0,0,0]	
	fifth = map(int, raw_input().split())
	sixth = [0,0,0,0,0,0]
	seventh = map(int, raw_input().split())
	eighth = [0,0,0,0,0,0,0,0]
	ninth = map(int, raw_input().split())
	
	matriz = [first, second, third, fourth, fifth, sixth, seventh,eighth, ninth]


	for j in range(2, len(matriz), 2):
		for k in range(1, j, 2):
			aux = (matriz[j-2][k-1] - matriz[j][k-1] - matriz[j][k])/2
			matriz[j].insert(k,aux)



	for l in range(1, len(matriz)-1, 2):
		for m in range(l+1):
			matriz[l][m] = matriz[l+1][m] + matriz[l+1][m+1]



	for o in range(len(matriz)):
		out = ""
		for p in range(len(matriz[o])):
			if (p == (len(matriz[o])-1)):
				out += str(matriz[o][p])
			else:
				out += str(matriz[o][p]) + " "

		print out
