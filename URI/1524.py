# https://www.urionlinejudge.com.br/judge/pt/problems/view/1524

#coding: utf-8

while True:
  try:
    n, k = map(int, raw_input().split())
    
    array = raw_input().split()
    
    aux = []
    
    aux.append(int(array[0]))
    
    for i in xrange(len(array)-1):
      aux.append(int(array[i+1]) - int(array[i]))
      
    answer = 0
    
    aux.sort()
    
    for i in xrange(n-k):
      answer += aux[i]
      
    print answer
    
  except:
    break
