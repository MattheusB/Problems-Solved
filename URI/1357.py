# https://www.urionlinejudge.com.br/judge/pt/problems/view/1357

#coding: utf-8

D = int(raw_input())


zero = [".*", "**", ".."]
one = ["*.", "..", ".."]
two = ["*.",  "*.", ".."]
three = ["**", "..", ".."]
four = ["**", ".*", ".."]
five = ["*.", ".*", ".."]
six = ["**", "*.", ".."]
seven = ["**", "**", ".."]
eight = ["*.", "**", ".."]
nine = [".*", "*.", ".."]

number_result = ""
result = ""

matriz = []

while D != 0:
	
	letter = raw_input()
	if (letter == "S"):
		number = raw_input()
		
		for i in range(D):
			if (number[i] == "1"):
				matriz.append(one)
				

			elif (number[i] == "2"):
				matriz.append(two)
				
			elif (number[i] == "3"):
				matriz.append(three)
				
			elif (number[i] == "4"):
				matriz.append(four)
				
			elif (number[i] == "5"):
				matriz.append(five)
				
			elif (number[i] == "6"):
				matriz.append(six)
				
			elif (number[i] == "7"):
				matriz.append(seven)
				
			elif (number[i] == "8"):
				matriz.append(eight)
				
			elif (number[i] == "9"):
				matriz.append(nine)
				
			elif (number[i] == "0"):
				matriz.append(zero)
				
		
		for k in range(3):
			for j in range(len(matriz)):
				if (j != (len(matriz) -1)):
					result += matriz[j][k] + " "
				else:
					result += matriz[j][k]
			if(k != 2):
				result += "\n"
			
		print result
	else:
		entrance1 = raw_input().split()
		entrance2 = raw_input().split()
		entrance3 = raw_input().split()
		
		for n in range(D):
			if (entrance1[n] == one[0] and entrance2[n] == one[1] and entrance3[n] == one[2]):
				number_result += "1"
		
			elif (entrance1[n] == two[0] and entrance2[n] == two[1] and entrance3[n] == two[2]):
				number_result += "2"
		
			elif (entrance1[n] == three[0] and entrance2[n] == three[1] and entrance3[n] == three[2]):
				number_result += "3"
		
			elif (entrance1[n] == four[0] and entrance2[n] == four[1] and entrance3[n] == four[2]):
				number_result += "4"
		
			elif (entrance1[n] == five[0] and entrance2[n] == five[1] and entrance3[n] == five[2]):
				number_result += "5"
		
			elif (entrance1[n] == six[0] and entrance2[n] == six[1] and entrance3[n] == six[2]):
				number_result += "6"
		
			elif (entrance1[n] == seven[0] and entrance2[n] == seven[1] and entrance3[n] == seven[2]):
				number_result += "7"
		
			elif (entrance1[n] == eight[0] and entrance2[n] == eight[1] and entrance3[n] == eight[2]):
				number_result += "8"
		
			elif (entrance1[n] == nine[0] and entrance2[n] == nine[1] and entrance3[n] == nine[2]):
				number_result += "9"
		
			elif (entrance1[n] == zero[0] and entrance2[n] == zero[1] and entrance3[n] == zero[2]):
				number_result += "0"
			
				
				
				
		print number_result
	
	matriz = []
	number_result = ""
	result = ""
				
	D = int(raw_input())
