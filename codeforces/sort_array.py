# https://codeforces.com/contest/451/problem/B

#coding: utf-8

n = int(raw_input())
a = map(int,raw_input().split())

verify1 = False
verify2 = False

i = 0
j = len(a) -1

index_begin = 0
index_end = 0

while (i <= j):
    if (verify1 == False):
        if(i == n-1):
            break
        elif(a[i] > a[i+1]):
            index_begin = i
            verify1 = True
        else:
            i += 1

    elif (verify2 == False):
        if(j == 0):
            break
        elif(a[j] < a[j-1]):
            index_end = j
            verify2 = True

        else:
            j -= 1
    else:
        break


k = index_begin
l = index_end

while (k < l):
    a[k], a[l] = a[l], a[k]
    k += 1
    l -= 1
        
isOrdered = True

for m in range(n-1):
    if (a[m] > a[m+1]):
        isOrdered = False
        break


if (isOrdered == True):
    print "yes"
    print index_begin +1, index_end +1
else:
    print "no"
