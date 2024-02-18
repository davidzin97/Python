
import random
numero_pc = random.randint(0,11)
numero = int(input('Número: '))
soma = numero_pc + numero
impapa = input('Impar ou Par? [I][P]').upper()
jogo = ''

if impapa == 'P':
    print('voce escolheu PAR')
elif impapa == 'I':
    print('voce escolheu IMPAR')
else:
    print('Você digitou um comando invalido')

if soma % 2 == 0:
    jogo = 'P'
    print('PAR')
else:
    jogo = 'I'
    print('IMPAR')
if impapa == jogo :
    print('PARABENS VOCE GANHOU')
else:
    print('VOCE PERDEU')
print('Você jogou {} a maquina jogou {} deu {}'.format (numero,numero_pc,jogo))

#jogo de impar ou par 