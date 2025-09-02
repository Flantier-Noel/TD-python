# exercice 7 : nv facile

""" vérifier si tout les élément de la liste L vérifie f:('a->bool) """

f = lambda x : (x%2)==0
L = [2, 4, 6, 7, 8]

all_true = ...
for i in range(len(L)):
    val = ...
    is_true = ...
    all_true = ... and ...

print(all_true)