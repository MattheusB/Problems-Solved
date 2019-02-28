# https://codeforces.com/contest/560/problem/A

#coding: utf-8

n = int(raw_input())

banknotes = map(int, raw_input().split())

if (1 in banknotes):
    print -1

else:
    print 1
