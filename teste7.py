import random
numero = random.randint(0,5)
adivinha = int(input('Adivinhe o Numero !  '))
if adivinha != numero:
    print('VOCE ERROU')
else:
    print('Parabens voce Acertou !')
print(numero)

#Jogo de adivinhar o numero 30/09/2023