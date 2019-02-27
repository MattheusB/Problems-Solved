# https://www.urionlinejudge.com.br/judge/pt/problems/view/1136

#coding: utf-8

def verify(answer, array, number):
	for i in range(len(array)):
		
		if (abs(number - array[i]) in answer):
			answer.remove(abs(number - array[i]))
			
	return answer
	

n, b = map(int, raw_input().split())

while n != 0 and b != 0:
	
	array = sorted(map(int, raw_input().split()))
	
	answer = range(0, n + 1)
	
	for j in range(b):
		
		answer = verify(answer, array, array[j])
		
	if (len(answer) == 0):
		print "Y"
	else:
		print "N"
		
	n, b = map(int, raw_input().split())
