lei = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

jac = input('Número: ')

if jac.isdigit():
    jac = int(jac)
    if 0 <= jac <= 20:
        print(lei[jac])
    else:
        print("Número fora do intervalo de 0 a 20")
else:
    print("Entrada inválida. Digite um número de 0 a 20.")

#progama vai ler o nome do numero , fiz de acordo com a posiçao na tupla
