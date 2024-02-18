
numeros = []
while True:
    numeros.append(int(input('Adicione um valor ')))
    resp = str(input ('quer continuar ? [S][N]')).upper()
    if resp == 'N':
        break
print(30*'=')
print(f'Voce digitou {len(numeros)} valores')
print(numeros)
numeros.sort(reverse=True)
if 5 in numeros:
    print('o valor 5 faz parte da lista')
else:
    print('o valor 5 não faz parte da lista')

    # checa quantos numeros voce colocou e se o numero 5 ta na lista 