# https://codeforces.com/contest/659/problem/A

entrada = raw_input().split(" ")

a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

saida = (b+c) % a

if (saida == 0):
    saida = a

print saida
