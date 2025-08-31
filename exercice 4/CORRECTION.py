## exercice 3 : nv facile

""" calculer le Ne terme de la suite : Fibo_0 = 0, Fibo_1 = 1, Fibo_{n+2} = Fibo_{n+1} + Fibo_{n} """

N = 4

Fibo0 = 0
Fibo1 = 1
for i in range(N) :
    mem = Fibo1
    Fibo1 = Fibo0 + Fibo1
    Fibo0 = mem

Fibo0 = 0
Fibo1 = 1
for i in range(N) :
    Fibo0, Fibo1 = Fibo1, Fibo0 + Fibo1

#

Fibo_lst = [0, 1]
for _ in range(N) :
    Fibo = Fibo_lst[-1] + Fibo_lst[-2]
    Fibo_lst.append(Fibo)

import matplotlib.pyplot as plt

Ind = [i for i in range(N+1)]
plt.plot(Ind, Fibo, 'rx')
plt.title("Valeurs de u_n - pour n <= N")
plt.show()


print(Fibo1) # on veut u_{N}