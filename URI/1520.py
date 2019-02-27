# https://www.urionlinejudge.com.br/judge/pt/problems/view/1520

#coding:utf-8
while True:
	try:
		n = raw_input()

		if (n != ""):
			nuts = []
			for i in range(int(n)):
				x, y = map(int, raw_input().split())
				for j in range(x, y+1):
					nuts.append(j)

			nuts = sorted(nuts)
      
			num = int(raw_input())
      
			i = 0
      
			while i < len(nuts) and nuts[i] != num:
				i += 1
      
			if i == len(nuts):
				print "%d not found" %num
			else:
				aux = len(nuts) -1
				while aux >= 0 and nuts[aux] != num:
					aux -= 1 
				print "%d found from %d to %d" %(num, i, aux)
    
	except EOFError:
		break
