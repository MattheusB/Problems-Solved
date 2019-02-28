# https://codeforces.com/contest/660/problem/A

#coding: utf-8

def calculate_mdc(number1, number2):
    if (number2 == 0):
        return number1

    else:
        return calculate_mdc(number2, number1%number2)


n = int(raw_input())

numbers = map(int, raw_input().split())

answer = ""

cont = 0

for i in range(n-1):
    mdc = calculate_mdc(numbers[i], numbers[i+1])
    
    answer += str(numbers[i]) + " "
    
    if (mdc != 1):
        answer += "1 "
        cont += 1

answer += str(numbers[len(numbers) -1])


print cont

print answer   
