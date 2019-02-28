# https://codeforces.com/contest/514/problem/B

#coding: utf-8

n, x0, y0 = map(int, raw_input().split())

storms = []

for i in xrange(n):
    storms.append(map(int, raw_input().split()))



shots = 0

for j in xrange(n):
    if storms[j]:
        target = storms[j]
        shots += 1
        storms[j] = False
        
        k = j + 1

        while k < n:
            main_target = storms[k]
            if main_target:
                if (((target[0] - x0) * (main_target[1] - y0)) == ((main_target[0] - x0) * (target[1] - y0))):
                    storms[k] = False

            k += 1

print shots        

