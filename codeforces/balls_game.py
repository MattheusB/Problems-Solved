# https://codeforces.com/contest/430/problem/B

#coding: utf-8

n, k, x = map(int, raw_input().split())

numbers = map(int, raw_input().split())

balls_values = [numbers[0]]
equals_balls = [1]
deleted_balls = []


for i in range(n-1):
    if(numbers[i] == numbers[i+1]):
        equals_balls[-1] += 1
    else:
        balls_values.append(numbers[i+1])
        equals_balls.append(1)

for j in range(len(equals_balls)):
    if(balls_values[j] == x and equals_balls[j] > 1):
        deleted_balls .append(equals_balls[j])
        pivot_before = j - 1
        pivot_after = j + 1

    
        while (pivot_before > -1 and pivot_after < len(equals_balls) and balls_values[pivot_before] == balls_values[pivot_after] and (equals_balls[pivot_before] + equals_balls[pivot_after]) > 2):
            deleted_balls[-1] += (equals_balls[pivot_before] + equals_balls[pivot_after])
            pivot_before -= 1
            pivot_after += 1


if (len(deleted_balls) != 0):
    print max(deleted_balls)
else:
    print 0
