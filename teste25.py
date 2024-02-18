numero1 = int(input('Primeiro numero? '))
numero2 = int(input('Segundo numero? '))

print('-------- O QUE VOCÊ DESEJA FAZER AGORA? --------')

print('[1] SOMAR')
print('[2] MULTIPLICAR')
print('[3] MAIOR')
print('[4] NOVOS NUMEROS')
print('[5] SAIR DO PROGAMA')

decida = int(input(''))
res = ''

if decida == 1:
    res = numero1 + numero2
    print('A Soma entre {} e {} é "{}"'.format(numero1,numero2,res))

elif decida == 2:
    res = numero1 * numero2
    print('A Multiplicação entre {} e {} é "{}"'.format(numero1,numero2,res))

elif decida == 3:
    if numero1 > numero2 :
        res = numero1
    else: res = numero2
    print('O numero maior é "{}"'.format(res))

elif decida == 4:
    print('Informe os numeros novamente')
    numero1 = int(input('Primeiro numero? '))
    numero2 = int(input('Segundo numero? '))

elif decida == 5 :
    print ('SAIU COM SUCESSO')

else:
    print('VALOR INVALIDO')    

# Pequeno progama de calculo !


#abaixo uma correão desse meu codigo

''''while True:
    numero1 = int(input('Primeiro numero? '))
    numero2 = int(input('Segundo numero? '))

    print('-------- O QUE VOCÊ DESEJA FAZER AGORA? --------')
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NUMEROS')
    print('[5] SAIR DO PROGRAMA')

    decida = int(input(''))

    if decida == 1:
        res = numero1 + numero2
        print('A Soma entre {} e {} é "{}"'.format(numero1, numero2, res))

    elif decida == 2:
        res = numero1 * numero2
        print('A Multiplicação entre {} e {} é "{}"'.format(numero1, numero2, res))

    elif decida == 3:
        if numero1 > numero2:
            res = numero1
        else:
            res = numero2
        print('O numero maior é "{}"'.format(res))

    elif decida == 4:
        print('Informe os numeros novamente')
        numero1 = int(input('Primeiro numero? '))
        numero2 = int(input('Segundo numero? '))

    elif decida == 5:
        print('SAIU COM SUCESSO')
        break

    else:
        print('VALOR INVALIDO')
'''