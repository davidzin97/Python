import random

nu1 = random.randint(0,100)
nu2 = random.randint(0,100)
nu3 = random.randint(0,100)
nu4 = random.randint(0,100)
nu5 = random.randint(0,100)

numero = (nu1 , nu2 , nu3 , nu4, nu5)
print (numero)

maior = nu1 

if nu2 > maior:
    maior = nu2

if nu3 > maior:
    maior = nu3

if nu4 > maior:
    maior = nu4

if nu5 > maior:
    maior = nu5

print('O número maior é', maior)

menor = nu1

if nu2 < menor:
    menor = nu2

if nu3 < menor:
    menor = nu3

if nu4 < menor:
    menor = nu4

if nu5 < menor:
    menor = nu5 

print('O numero menor é ',menor)

#progama que gera 5 numeros e fala qual é o maior e qual é o menor