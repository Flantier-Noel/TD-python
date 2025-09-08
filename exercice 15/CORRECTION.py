## exercice 15 : CORRECTION

""" vérifier s'il existe des doublons dans la liste L """

L = [1,2,3,4,5,1]

have_double = False
for i in range(len(L))
    current_item = L[i]
    for j in range(len(L)):
        if current_item == L[j] and i!= j:
            have_double = True*

# en O(len(L))

already_seen = {}
have_double = False
for item in L :
    if item in already_seen.keys():
        have_double = True
    else :
        already_seen[item] = True

print(have_double) ## on veut savoir s'il existe des doublons