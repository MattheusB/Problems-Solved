# https://www.urionlinejudge.com.br/judge/pt/problems/view/1029

# -*- coding: utf-8 -*-

def fibonacci(number):
	result = [0, 1]
	calls = [0, 0]
	for i in xrange(2, number + 1):
		result.append(result[i - 1] + result[i - 2])
		calls.append(calls[i - 1] + calls[i - 2] + 2)
	return calls[number], result[number]

num_calls = int(raw_input())
for i in range(num_calls):
	number = int(raw_input())
	result, calls = fibonacci(number)
	print "fib(%i) = %i calls = %i" %(number, result, calls)
 
