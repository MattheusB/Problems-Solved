# https://www.urionlinejudge.com.br/judge/pt/problems/view/1009

VENDEDOR = str(raw_input())
FIXO = float(raw_input())
VENDAS = float(raw_input())
TOTAL = FIXO + (VENDAS*0.15)
print "TOTAL = R$ %.2f"%(TOTAL)
