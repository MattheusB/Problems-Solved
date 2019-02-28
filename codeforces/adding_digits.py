# https://codeforces.com/contest/260/problem/A

#coding: utf-8

array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

number1, number2, n = raw_input().split()

number2 = int(number2)
n = int(n)

aux = number1

for i in range(len(array)):
    if(int(number1+array[i])%number2 == 0):
        number1 += array[i]
        break

if(aux == number1):
    print -1

else:
    for j in range(n-1):
        number1 += "0"

    print number1
     
