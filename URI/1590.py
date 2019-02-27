# https://www.urionlinejudge.com.br/judge/pt/problems/view/1590

#coding: utf-8

from itertools import combinations

t = int(raw_input())

while (t > 0):
	try:
		n, k = map(int, raw_input().split())
		
		numbers = map(int, raw_input().split())
		
		if (len(numbers) < k):
			print 0
		
		else:
			r = 0
			
			for i in range(30,-1,-1):
				
				inList = []
				notList = []
				q = 0
				
				bitDeslocado = 1 << i
				
				for j in range(len(numbers) - 1,-1,-1):
					
					if (bitDeslocado & numbers[j]):
						inList.append(j)
						q += 1
					else:
						notList.append(j)
				
				if (q >= k):	
					
					aux = numbers[inList[0]]
					
					for l in range(1,q):
						aux &= numbers[inList[l]]
						
					r = max(r, aux)
				
					for m in range(len(notList)):
						del numbers[notList[m]]
					
					
			print r
		t -= 1
		
	except EOFError:
		break
