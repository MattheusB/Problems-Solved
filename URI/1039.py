# https://www.urionlinejudge.com.br/judge/pt/problems/view/1039

#coding: utf-8
from math import sqrt

while True:
    try:
        r1, x1, y1, r2, x2, y2 = map(int, raw_input().split()) 
       
        distance = sqrt((x1 - x2)**2 + (y1 - y2)**2)
        
        if(distance + r2 <= r1):
            print "RICO"
        else:
            print "MORTO"
    except:
           break
