## exercice 13 : CORRECTION

""" décomposer X en base n """

X = 372
n = 7

rest = X
pow_ind = 0
decomp = []
while rest > 0 :
    val = rest % (n**pow_ind)
    rest = rest - val
    pow_ind += 1
    decomp.append(val)

# SANS calcul des (n^i)_i

rest = X
decomp = []
while rest > 0 :
    val = rest % n
    rest = (rest - val)//n
    decomp.append(val)

print(decomp) # on veut [1, 4, 0, 1]