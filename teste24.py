import random
numero = random.randint(0, 10)
adivinha = int(input('Adivinhe o número! '))
tentativas = 1

while adivinha != numero: # enquanto o numero for diferente do adivinha 
    print('VOCÊ ERROU')
    adivinha = int(input('Tente novamente: ')) 
    tentativas += 1

print('Parabéns, você acertou!')
print('O número é', numero)
print('Voce tentou {} vezes'.format(tentativas))

# Jogo de adivinhar o numero 2.0 fo colocado o tanto de vezes que foi tentado !