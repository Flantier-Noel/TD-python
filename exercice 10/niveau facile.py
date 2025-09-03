## exercice 10 : nv facile

""" le but est de trier la liste L dans l'ordre croissant """

L = [2, 5, 3, 1, 8, 12]

def merge(L1:list, L2:list):
    i1, i2 = 0
    L_merge = []
    while i1 < ... and i2 < ... :
        if i1 > ... :
            L_merge.append(...)
            i2 = ...
        elif i2 > ... :
            L_merge.append(...)
            i1 = ...
        elif ... :
            L_merge.append(...)
            i2 = ...
        else :
            L_merge.append(...)
            i1 = ...
    return L_merge

def sort(L0):
    if len(L0) <= ... :
        return L0
    else :
        ind_mid = ...
        L1, L2 = ...
        L1_sorted, L2_sorted = ...
        return merge(...)

print(sort(L)) # on veut sorted(L)