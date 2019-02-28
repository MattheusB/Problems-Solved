# https://codeforces.com/contest/467/problem/B

#coding: utf-8

n, m, k = map(int,raw_input().split())
answer = 0
players = []

for i in range(m + 1):
	
	players.append(int(raw_input()))

for j in range(m):
	
	if (str(bin(players[m] ^ players[j])).count("1") <= k):
		answer += 1

print answer
