# https://codeforces.com/contest/445/problem/B

#coding: utf-8
n, m = map(int, raw_input().split())
aux = [0]*(n+1)
for i in xrange(1, n + 1):
    aux[i] = i

answer = 1

while (m > 0):
    m -= 1

    a, b = map(int, raw_input().split())
    while (aux[a] != a or b != aux[b]):
        a = aux[a]
        b = aux[b]

    if (a != b):
        answer *= 2

    if (a < b):
        aux[a] = aux[b] = a
    else:
        aux[a] = aux[b] = b

print answer
