# https://www.urionlinejudge.com.br/judge/pt/problems/view/1905

#coding: utf-8



global checked
global matrix


	

n = int(raw_input())


def matrixPath(i,j):
	if (i >=0 and i < 5 and j >= 0 and j < 5):
		if (matrix[i][j] == "0" and checked[i][j] == False):
			checked[i][j] = True
			
			matrixPath(i, j+1)
			matrixPath(i, j-1)
			matrixPath(i+1, j)
			matrixPath(i-1, j)

for i in range(n):
	
	matrix = []
	
	while (len(matrix) < 5):
		lineAux = raw_input().split()
		if (len(lineAux) > 0):
			matrix.append(lineAux)
		
		
	checked = [[False for i in range(5)] for j in range(5)]
				
	matrixPath(0,0)
	
	

	if (checked[4][4] ==  True):
		print "COPS"
	else:
		print "ROBBERS"
	
	
