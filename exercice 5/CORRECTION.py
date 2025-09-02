## exercie 5 : CORRECTION

""" trouver le minimum de la liste L d'entier """

L = [1, 4, 3, 8, 57, 4]

val_min = L[0]

for i in range(len(L)):
    val_cur = L[i]
    if val_cur < val_min :
        val_min = val_cur

print(val_min) # on veut min(L)

""" trouver le minimum de la liste L d'entier, et un indice d'atteinte  """


val_min = L[0]
ind_min = 0

for i in range(len(L)):
    val_cur = L[i]
    if val_cur < val_min :
        val_min = val_cur
        ind_min = i

print(val_min, ind_min) # on veut min(L) et i tq L[i] = min(L)