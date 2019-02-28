# https://codeforces.com/contest/18/problem/C

#coding: utf-8
amount = int(raw_input())
numbers = map(int, raw_input().split())

all_sum = 0
partial_sum = numbers[0]

possibilities = 0

for i in range(1,amount):
    all_sum += numbers[i]


for j in range(1, amount):
    if (partial_sum == all_sum):
        possibilities += 1
        all_sum -= numbers[j]
        partial_sum += numbers[j]
    
    else:
        partial_sum += numbers[j]
        all_sum -= numbers[j]
    

print possibilities
