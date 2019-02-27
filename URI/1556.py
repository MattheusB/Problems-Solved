# https://www.urionlinejudge.com.br/judge/pt/problems/view/1556

#coding: utf-8


def removeLetra(word):
	
	
	global wordSet
	
	if (len(word) < 3):
		return;
		
	for i in range(len(word)):
		wordAux = word[:i] + word[i+1:]
		lenWord = len(wordSet)
		
		wordSet.add(wordAux)
		
		if (lenWord < len(wordSet)):
			removeLetra(wordAux)


while True:
	try:
		word = raw_input()
		wordArray = []
		wordSet = set()
		
		wordSet.add(word)
	
		
		for i in range(len(word)):
			wordSet.add(word[i])
	
		removeLetra(word)
		
		
		for item in wordSet:
			wordArray.append(item)
			
		wordArray.sort()
		
		for j in range(len(wordArray)):
			print wordArray[j]
		
		print
	except EOFError:
		break;
