# https://codeforces.com/contest/624/problem/A

#coding: utf-8

d, L, v1, v2 = map(int,raw_input().split())

answer = float(L-d)/float(v1+v2)

print "%.20f" %answer
