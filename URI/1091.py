# https://www.urionlinejudge.com.br/judge/pt/problems/view/1091

#coding: utf-8

K = int(raw_input())

while K != 0:
	currency = raw_input().split()
	
	for i in range(K):
		coordinate = raw_input().split()
		
	
		if (int(coordinate[0]) == int(currency[0]) or int(coordinate[1]) == int(currency[1])):
			print "divisa"
	
		elif (int(coordinate[0]) < int(currency[0]) and int(coordinate[1]) > int(currency[1])):
			print "NO"
		
		elif (int(coordinate[0]) > int(currency[0]) and int(coordinate[1]) > int(currency[1])):
			print "NE"
		
		elif (int(coordinate[0]) > int(currency[0]) and int(coordinate[1]) < int(currency[1])):
			print "SE"
		
		elif (int(coordinate[0]) < int(currency[0]) and int(coordinate[1]) < int(currency[1])):
			print "SO"
		
	K = int(raw_input())
