# https://www.urionlinejudge.com.br/judge/pt/problems/view/1235

#coding: utf-8

n = int(raw_input())


for i in xrange(n):
    out = ""
    aux = raw_input()
    for j in xrange(len(aux)/2 -1, -1, -1):
        out += aux[j]
    
    for k in xrange(len(aux) -1, len(aux)/2-1, -1):
        out += aux[k]
        
    print out

