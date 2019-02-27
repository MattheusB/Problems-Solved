# https://www.urionlinejudge.com.br/judge/pt/problems/view/1026

#coding: utf-8

while True:
	try:
		number1, number2 = map(int, raw_input().split())
		
		answer = number1^number2
		
		print answer
		
	except:
		break
