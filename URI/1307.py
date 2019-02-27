# https://www.urionlinejudge.com.br/judge/pt/problems/view/1307

#coding: utf-8

def verifyNumber (s1, s2):
    if (s2 == 0):
        return s1
    else:
        return verifyNumber(s2, s1%s2)

pairs = int(raw_input())


for i in range(1,pairs + 1):
    string1 = raw_input()
    string2 = raw_input()
    
    
    answer = verifyNumber(int(string1,2), int(string2,2))
   
 
    if (answer > 1):
        print "Pair #%d: All you need is love!" %(i)

    else:
        print "Pair #%d: Love is not all you need!" %(i)
    
