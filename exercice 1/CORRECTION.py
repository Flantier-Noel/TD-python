## exercice 1 : correction

""" étant donnés les entiers a et b, inverser leurs valeurs """

a = 57
b = 21

#

c = a
a = b
b = c

#

a,b = b,a

#

a = a^b
b = a^b
a = a^b

print(a,b)