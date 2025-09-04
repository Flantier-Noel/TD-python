## exercice 11 : CORRECTION

""" le but est de calculer a**n """

a = 2
n = 10

result = 1
for i in range(n):
    result = result*n

print(result) # on veut a**n

def fast_pow(x, k):
    if k==0 : return 1
    if k==1 : return x
    return fast_pow(x, k//2)*fast_pow(x, k-k//2)

print(fast_pow(a, n)) # on veut a**n