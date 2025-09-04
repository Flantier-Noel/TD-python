## exercice 12 : nv moyen

""" le but est de trouver un point d'annulation de f:('float->'float) par dichotomie dans [a,b] """

f = lambda x : x**3 - 2*x - 2
a, b = 0, 1 # on suppose f(a)<f(b)
precis = 1e-5 # précision d'arrêt de la dichtomie

mid = ...
while ... :
    if ... :
        a, b = ...
    else :
        a, b = ...
    
    mid = ...

return mid # on veut un point d'annulation de f