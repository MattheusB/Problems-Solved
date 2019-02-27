# https://www.urionlinejudge.com.br/judge/pt/problems/view/1025

#coding: utf-8

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
          while target == array[x]:
            x-=1 
          x+=1 
          return x
        elif target > val:
            if lower == x:   
                break        
            lower = x
        elif target < val:
            upper = x

entrada = raw_input().split(" ")
n, q = int(entrada[0]), int(entrada[1])
serial = 1
while n != 0 and q != 0:
  marbles = []
  i = 0
  while i != n:
    marbles.append(int(raw_input()))
    i += 1
  marbles.sort()
