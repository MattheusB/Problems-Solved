# https://www.urionlinejudge.com.br/judge/pt/problems/view/1878

#coding: utf-8



def verifyDenis(students, c1, c2, c3):
	global possibilities
	possibilities = set()
	
	for i in range(1, students + 1):
		for j in range(1, students + 1):
			for k in range(1, students + 1):
				result = (i * c1) + (j * c2) + (k * c3)
				possibilities.add(result)



while True:
	try:
		n, m = map(int, raw_input().split())

		c = map(int, raw_input().split())

		if (n == 1):
			verifyDenis(m, c[0], 0, 0)
		elif (n == 2):
			verifyDenis(m, c[0], c[1], 0)
		else:
			verifyDenis(m, c[0], c[1], c[2])
			
		answer = len(possibilities)
			
		if (answer == (m ** n)):
			print "Lucky Denis!"
		else:
			print "Try again later, Denis..."
		
		
		
	except EOFError:
		break;

