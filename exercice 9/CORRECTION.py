## exercice 9 : CORRECTION

""" le but est de trier la liste L dans l'ordre croissant """

L = [2, 5, 3, 1, 8, 12]

for i in range(len(L)):
    ind_min = i
    for j in range(i, len(L)):
            if L[j] < L[ind_min] :
                ind_min = j

    L[i], L[ind_min] = L[ind_min], L[i]

print(L) # on veut sorted(L)