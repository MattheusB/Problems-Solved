# https://www.urionlinejudge.com.br/judge/pt/problems/view/1049

#coding: utf-8


tipo1 = raw_input()
tipo2 = raw_input()
tipo3 = raw_input()

if (tipo1 == "vertebrado"):
    if (tipo2 == "ave"):
        if (tipo3 == "carnivoro"):
            print "aguia"
        else:
            print "pomba"

    else:
        if (tipo3 == "onivoro"):
            print "homem"
        else:
            print "vaca"

else:
    if (tipo2 == "inseto"):
        if (tipo3 == "hematofago"):
            print "pulga"
        else:
            print "lagarta"
    else:
        if (tipo3 == "hematofago"):
            print "sanguessuga"
        else:
            print "minhoca"
