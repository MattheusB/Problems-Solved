# https://www.urionlinejudge.com.br/judge/pt/problems/view/1170

#coding: utf-8

def divide_supplies(number):
    if number == 0:
        return 0

    elif number <= 1:
        return 0

    else:
        return 1 + divide_supplies(number/2)


n = int(raw_input())

for i in range(n):
    c = float(raw_input())
    print str(divide_supplies(c)) + " dias"

