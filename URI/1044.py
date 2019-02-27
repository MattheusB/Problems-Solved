# https://www.urionlinejudge.com.br/judge/pt/problems/view/1044

#coding: utf-8

entrada = raw_input().split(" ")

A = int(entrada[0])
B = int(entrada[1])

maior = 0
menor = 0

if (A > B):
    maior = A
    menor = B

else:
    maior = B
    menor = A 

if (maior%menor == 0):
    print "Sao Multiplos"
else:
    print "Nao sao Multiplos"
