# https://www.urionlinejudge.com.br/judge/pt/problems/view/1796

#coding: utf-8


Q = int(raw_input())
V = raw_input().split(" ")

satisfeitos = 0
insatisfeitos = 0

for i in range(Q):
    if(V[i] == "0"):
        satisfeitos += 1
    else:
        insatisfeitos += 1


if (insatisfeitos >= satisfeitos):
    print "N"
else:
    print "Y"
