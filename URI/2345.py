# https://www.urionlinejudge.com.br/judge/pt/problems/view/2345

#coding: utf-8

A, B, C, D = map(int, raw_input().split())

lista = [A, B, C, D]

lista.sort()

equipe1 = lista[0] + lista[3]

equipe2 = lista[2] + lista[1]

print abs(equipe1 - equipe2)

