# https://www.urionlinejudge.com.br/judge/pt/problems/view/1898

#coding: utf-8

numbers = ["0","1","2","3","4","5","6","7","8","9"]

entrance1 = raw_input()
entrance2 = raw_input()

number1 = ""

aux1 = ""

number2 = ""

cont = 0

verify = False

for i in range(len(entrance1)):
        if (cont == 2):
            break

        elif (verify == True):
            if (entrance1[i] in numbers):
                aux1 += entrance1[i]
                cont += 1

        elif(entrance1[i] == "."):
           aux1 += entrance1[i]
           verify = True

        elif(entrance1[i] in numbers):
            if(len(number1) < 11):
                number1 += entrance1[i]
            else:
                aux1 += entrance1[i]

cont = 0
verify = False

for j in range(len(entrance2)):
    if (cont == 2):
        break
    elif(verify == True):
        if (entrance2[j] in numbers):
            number2 += entrance2[j]
            cont += 1
    
    elif(entrance2[j] in numbers):
        number2 += entrance2[j]
        
    elif(entrance2[j] == "."):
        number2 += entrance2[j]
        verify = True

soma = float(aux1) + float(number2)

print "cpf %s" %(number1)

print "%.2f" %(soma)

