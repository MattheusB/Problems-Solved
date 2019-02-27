# https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

peca1 = raw_input().split()
a = int(peca1[0])
b = int(peca1[1])
c = float(peca1[2])
peca2 = raw_input().split()
a2 = int(peca2[0])
b2 = int(peca2[1])
c2 = float(peca2[2])
total = (b*c) + (b2*c2)
print "VALOR A PAGAR: R$ %.2f" %total
