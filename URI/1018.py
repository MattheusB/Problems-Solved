# https://www.urionlinejudge.com.br/judge/pt/problems/view/1018

#coding: utf-8

cem = 0
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0

entrada = int(raw_input())

print entrada

while entrada > 0:
    if (entrada >= 100):
        cem += 1
        entrada -= 100
    elif (entrada >= 50):
        cinquenta += 1
        entrada -= 50
    elif (entrada >= 20):
        vinte += 1
        entrada -= 20
    elif (entrada >= 10):
        dez += 1
        entrada -= 10
    elif (entrada >= 5):
        cinco += 1
        entrada -= 5
    elif (entrada >= 2):
        dois += 1
        entrada -= 2
    else:
        um += 1
        entrada -= 1

print "%i nota(s) de R$ 100,00" %(cem)
print "%i nota(s) de R$ 50,00" %(cinquenta)
print "%i nota(s) de R$ 20,00" %(vinte)
print "%i nota(s) de R$ 10,00" %(dez)
print "%i nota(s) de R$ 5,00" %(cinco)
print "%i nota(s) de R$ 2,00" %(dois)
print "%i nota(s) de R$ 1,00" %(um)
