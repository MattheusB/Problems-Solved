# https://www.urionlinejudge.com.br/judge/pt/problems/view/1802

#coding: utf-8


out = []

p = map(int, raw_input().split())
m = map(int, raw_input().split())
f = map(int, raw_input().split())
q = map(int, raw_input().split())
b = map(int, raw_input().split())

p = p[1::]
m = m[1::]
f = f[1::]
q = q[1::]
b = b[1::]



for i in p:
    for j in m:
        for k in f:
            for l in q:
                for n in b:
                    out.append(i + j + k + l + n)

out.sort()

number = int(raw_input())


soma = 0
i = 0
while i < number:
    soma += out[len(out)-1-i]
    i += 1

print soma
