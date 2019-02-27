# https://www.urionlinejudge.com.br/judge/pt/problems/view/1012

ent = raw_input().split()
A = float(ent [0])
B = float(ent [1])
C = float(ent [2])
pi = 3.14159
TRIANGULO = (A*C)/2
CIRCULO = pi * (C**2)
TRAPEZIO = ((A+B)*C)/2
QUADRADO = B**2
RETANGULO = (A*B)
print "TRIANGULO: %.3f" %TRIANGULO
print "CIRCULO: %.3f" %CIRCULO
print "TRAPEZIO: %.3f" %TRAPEZIO
print "QUADRADO: %.3f" %QUADRADO
print "RETANGULO: %.3f" %RETANGULO
