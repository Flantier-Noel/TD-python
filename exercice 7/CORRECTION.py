# exercice 7 : CORRECTION

""" vérifier si tout les élément de la liste L vérifie f:('a->bool) """

f = lambda x : (x%2)==0
L = [2, 4, 6, 7, 8]

all_true = True
for i in range(len(L)):
    val = L[i]
    is_true = f(val)
    all_true = all_true and is_true

print(all_true)