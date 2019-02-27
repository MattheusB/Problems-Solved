# https://www.urionlinejudge.com.br/judge/pt/problems/view/1429

#coding: utf-8


values = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
number = raw_input()


while (number != "0"):
	answer = 0
	for i in xrange(len(number)):
		answer += int(number[i]) * values[len(number) - i]
	
	print answer
	number = raw_input()
		
