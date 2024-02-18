#a tabuada se encerra quando se coloca um numero negativo

print('-' * 30)

while True:
    numero = int(input('Qual a tabuada você quer saber? '))
    
    if numero < 0:
        break

    for x in range(1, 11):
        print('{} x {} = {}'.format(numero, x, numero * x))
print('Voce saiu da tabuada')

#criando uma condiao para sair da tabuada