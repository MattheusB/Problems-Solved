# https://www.urionlinejudge.com.br/judge/pt/problems/view/1099

#coding: utf-8

n = int(raw_input())
for i in range(n):
	x, y = map(int, raw_input().split())
	if (y > x):
		aux = x
		x = y
		y = aux

	answer = 0
	for j in range(y+1, x):
		if (j %2 != 0):
			answer += j
	print answer
