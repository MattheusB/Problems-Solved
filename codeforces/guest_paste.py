# https://codeforces.com/contest/625/problem/A

#coding: utf-8

cash = int(raw_input())

plastic = int(raw_input())
glass = int(raw_input())
return_glass = int(raw_input())

bottles = 0

if (cash >= glass and (glass - return_glass) <= plastic):
    bottles = (cash - glass)/(glass - return_glass) + 1
    cash -= bottles *(glass - return_glass)


bottles += cash/plastic

print bottles
