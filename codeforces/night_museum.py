# https://codeforces.com/contest/731/problem/A

#coding: utf-8

name = raw_input()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

position = 0

rotations = 0

average = len(alphabet)/2

for i in range(len(name)):
	index = alphabet.index(name[i])
	
	result = abs(position - index)
	
	if(result < average):
		rotations += result
		
	else:
		rotations += len(alphabet) - result
		
	position = index
	
	
print rotations
