## exercice 6 : CORRECTION

""" appliquer la fonction f:('a->'a) a tout les éléments de la liste L """

f = lambda x : 2*x
L = [2, 3, 5, 7, 11, 13]

new_L = []
for i in range(len(L)):
    val = L[i]
    new_L.append(f(L[i]))

#

new_L = [f(val) for val in L]

print(new_L) # on veut f(L)

# en place

for i in range(len(L)):
    L[i] = f(L[i])

print(L) # on veut f(L)