# https://www.urionlinejudge.com.br/judge/pt/problems/view/1161

#coding: utf-8

def fatorial(number):
    if(number == 0):
        return 1
    
    return number*fatorial(number-1)

while True:
    try: 
        entrance = map(int, raw_input().split())
        print fatorial(entrance[0]) + fatorial(entrance[1])
    except:
           break
