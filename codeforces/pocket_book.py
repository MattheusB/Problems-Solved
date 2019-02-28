# https://codeforces.com/contest/152/problem/C

#coding: utf-8


n, m = map(int, raw_input().split())

letters = []
for a in range(m):
    aux = []
    letters.append(aux)


for i in range(n):
    word = raw_input()
    for j in range(m):
        if (word[j] not in letters[j]):
            letters[j].append(word[j])


sum = 1

for k in range(len(letters)):
    sum *= len(letters[k])




print sum % 1000000007 
