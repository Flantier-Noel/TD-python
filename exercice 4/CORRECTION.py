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


print(Fibo1) # on veut u_{N}