# https://www.urionlinejudge.com.br/judge/pt/problems/view/1068

#coding: utf-8

while True:
    try:
        entrance = raw_input()
        answer = ""    
        parentheses = []

        for i in range(len(entrance)):
            if (entrance[i] == "("):
                    parentheses.append("(")
            elif(entrance[i] == ")"):
                if (len(parentheses) != 0):
                    parentheses.remove("(")
                else:
                    answer = "incorrect"
        
        if (answer == ""):
            if(len(parentheses) == 0):
                answer = "correct"
            else:
                answer = "incorrect"

        print answer
    except:
        break

