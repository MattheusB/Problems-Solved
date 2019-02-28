# https://codeforces.com/contest/722/problem/A

#coding: utf-8

time_format1 = raw_input()
time_format2 = raw_input().split(":")

aux = ""


if (time_format1 == "12"):
	
	if(int(time_format2[0]) > 12):
		if(time_format2[0][1] == "0"):
			aux += "1"
		else:
			aux += "0"
		aux += time_format2[0][1]
		
	elif(int(time_format2[0]) < 1):
		aux += "0"
		aux += "1"
	else:
		aux += time_format2[0]
		
		
	aux += ":"
	
	if(int(time_format2[1]) > 59):
		aux += "0"
		aux += time_format2[1][1]
	else:
		aux += time_format2[1]
		
else:
	if(int(time_format2[0]) > 23):
		aux += "0"
		aux += time_format2[0][1]
	else:
		aux += time_format2[0]
	
	aux += ":"
	
	if(int(time_format2[1]) > 59):
		aux += "0"
		aux += time_format2[1][1]
	else:
		aux += time_format2[1]
print aux
		
