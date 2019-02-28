# https://codeforces.com/contest/576/problem/A

#coding: utf-8

import math

n = 10**3

primes = [True] * (n+1)

primes[0] = False
primes[1] = False

for i in range(2, int(math.sqrt(n)+1)):
    if (primes[i]):
        for j in range(i+i, n +1, i):
            primes[j] = False

number = int(raw_input())

asks = []

for k in range(1, number+1):
    if (primes[k]):
        l = 1
        while l <= (number / k):
            l *= k
            asks.append(l)


print len(asks)

for m in range(len(asks)):
    print asks[m],
