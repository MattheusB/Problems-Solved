# https://www.urionlinejudge.com.br/judge/pt/problems/view/2381

#coding: utf-8


n, k = map(int,raw_input().split())

alunos = []

for i in range(n):
    nome = raw_input()
    alunos.append(nome)




alunos.sort()


print alunos[k-1]

