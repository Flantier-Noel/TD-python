## exercice 10 : nv facile

""" le but est de trier la liste L dans l'ordre croissant """

L = [2, 5, 3, 1, 8, 12]

def merge(L1:list, L2:list):
    i1, i2 = 0
    L_merge = []
    while i1 < len(L1) and i2 < len(L2) :
        if i1 > len(L1) :
            L_merge.append(L2[i2])
            i2 = i2+1
        elif i2 > len(L2) :
            L_merge.append(L1[i1])
            i1 = i1+1
        elif L1[i1] > L2[i2] :
            L_merge.append(L2[i2])
            i2 = i2+1
        else :
            L_merge.append(l1[i1])
            i1 = i1+1
    return L_merge

def sort(L0):
    if len(L0) <= 1 :
        return L0
    else :
        ind_mid = len(L0)//2
        L1, L2 = L0[:ind_mid], L0[ind_mid:]
        L1_sorted, L2_sorted = sort(L1), sort(L2)
        return merge(L1_sorted, L2_sorted)

print(sort(L)) # on veut sorted(L)