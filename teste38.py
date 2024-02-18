num = [ [],[] ] # uma lista com mais duas listas dentro


for p in range(0,8):
    valor = (int(input('Numero ' )))
    if valor % 2 == 0 :
        num[0].append(valor)  # adiciona o valor na primeira lista dentro da lista
    else:
        num[1].append(valor) # adiciona o valor na segunda lista dentro de outras lista


print(num)
print(f'{num[0]}  numeros par')
print(f'{num[1]}  numeros impar')

# adiciona numeros dentro de uma lista e organiza impar e par dentro da mesma lista 