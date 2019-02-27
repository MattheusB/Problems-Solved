# https://www.urionlinejudge.com.br/judge/pt/problems/view/1028

#coding: utf-8

def calculate_mdc(number1, number2):
    if(number2 == 0):
        return number1
    else:
        return calculate_mdc(number2, number1%number2)


n = int(raw_input())

for i in range(n):
    number1, number2 = map(int, raw_input().split())

    mdc = calculate_mdc(number1, number2)

    print mdc

