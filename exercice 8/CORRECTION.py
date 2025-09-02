# exercice 8 : CORRECTION

""" vérifier si un des élément de la liste L vérifie f:('a->bool) """

f = lambda x : (x%2)==0
L = [2, 4, 6, 7, 8]

one_true = False
for i in range(len(L)):
    val = L[i]
    is_true = f(L[i])
    one_true = one_true and is_true

print(one_true)