# Exercice 14 : CORRECTION

""" trouver l'écriture décimale de X écrit en base n """

X = [1, 4, 0, 1]
n = 7

x_10 = 0

for i in range(len(X)):
    coeff_i = X[i]
    x_10 = x_10 + coeff_i*(n**i)

# SANS calcul des (n^i)_i

x_10 = 0
for i in range(len(X)-1, -1, -1)
    x_10 = n*x_10 + X[i]

print(x_10) # on veut 372