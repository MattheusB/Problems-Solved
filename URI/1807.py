# https://www.urionlinejudge.com.br/judge/pt/problems/view/1807

#coding: utf-8

def power(a, b):
    if(b == 0):
        return 1
    elif (b == 1):
        return a

    elif (b % 2 == 0):
        return power((a * a) % (2**31 -1), b/2)

    else:
        return (a * power((a * a) % (2**31 -1), (b -1) /2)) % (2**31 -1)




b = int(raw_input())

print power(3, b)

