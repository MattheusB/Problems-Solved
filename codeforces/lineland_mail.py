# https://codeforces.com/contest/567/problem/A

#coding: utf-8

number_cities = int(raw_input())

coordinate = raw_input().split()

mini = 0
maxi = 0

for i in range(number_cities):
	if (i == 0):
		
		mini = abs(int(coordinate[i]) - int(coordinate[i+1]))
		maxi = abs(int(coordinate[i]) - int(coordinate[number_cities-1]))
		print mini, maxi
	
	elif(i == (number_cities -1)):
		mini = abs(int(coordinate[i]) - int(coordinate[i-1]))
		maxi = abs(int(coordinate[i]) - int(coordinate[0]))
		print mini, maxi
	
	else:
		if(abs(int(coordinate[i]) - int(coordinate[i-1])) < abs(int(coordinate[i]) - int(coordinate[i+1]))):
			mini = abs(int(coordinate[i]) - int(coordinate[i-1]))
		else:
			mini = abs(int(coordinate[i]) - int(coordinate[i+1]))
			
		if(abs(int(coordinate[i]) - int(coordinate[0])) > abs(int(coordinate[i]) - int(coordinate[number_cities-1]))):
			maxi = abs(int(coordinate[i]) - int(coordinate[0]))
		else:
			maxi = abs(int(coordinate[i]) - int(coordinate[number_cities -1]))
		
		print mini, maxi
			
