## exercice 12 : nv facile

""" le but est de trouver un point d'annulation de f:('float->'float) par dichotomie dans [a,b] """

f = lambda x : x**3 - 2*x - 2
a, b = 0, 1 # on suppose f(a)<f(b)
precis = 1e-5 # précision d'arrêt de la dichtomie

mid = (a+b)/2
while f(mid) > precis :
    if f(mid) < 0 :
        a, b = a, mid
    else :
        a, b = mid, b
    
    mid = (a+b)/2

return mid # on veut un point d'annulation de f