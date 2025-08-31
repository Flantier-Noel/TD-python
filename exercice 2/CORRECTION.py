## exercice 2 : CORRECTION
""" calculer le Ne terme de la suite : u_0 = 5 et u_{n+1} = u_{n} + 12 """

N = 4

u = 5
for i in range(N) :
    u = u+12

#

u = 5
for i in range(N) :
    u += 12

#

U = [5]
for _ in range(N) :
    u = U[-1] + 12
    U.append(u)

print(u) # on veut u_{N}

import matplotlib.pyplot as plt

Ind = [i for i in range(N+1)]
plt.plot(Ind, U, 'rx')
plt.title("Valeurs de u_n - pour n <= N")
plt.show()