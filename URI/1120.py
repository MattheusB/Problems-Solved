# https://www.urionlinejudge.com.br/judge/pt/problems/view/1120

#coding: utf-8


d, n = raw_input().split()


while d != "0" and n != "0":
	
	answer = ""
	for i in range(len(n)):
		if (n[i] != d):
			if (len(answer) != 0 or n[i] != "0"):
				answer += n[i]
				
	if (len(answer) == 0):
		print "0"
	else:
		print answer
	
	d, n = raw_input().split()
		
