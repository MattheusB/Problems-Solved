# https://codeforces.com/contest/732/problem/A

#coding: utf-8

price_shovel, coin = map(int, raw_input().split())

i = 1

while i < 11:

    if ((price_shovel * i)%10 == 0 or (price_shovel * i)%10 == coin):
        print i
        break

    i += 1
