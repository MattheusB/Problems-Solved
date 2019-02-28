# https://codeforces.com/contest/580/problem/B

#coding: utf-8


friends, limit = map(int, raw_input().split())

matrix = []

for i in range(friends):
    matrix.append(map(int, raw_input().split()))

partial_sum = 0

greater_sum = 0

k = 0

matrix.sort()


for j in range(friends):
    
    while k < friends and abs(matrix[k][0] - matrix[j][0]) < limit:
        partial_sum += matrix[k][1]
        k += 1

    if (partial_sum > greater_sum):
        greater_sum = partial_sum

    partial_sum -= matrix[j][1]
        


print greater_sum
