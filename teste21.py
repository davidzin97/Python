maior = 0
menor = 0

for p in range (1,6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(p)))
    if p == 1 :
        maior = peso
        menor = peso
    else :
        if peso > maior:
           maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi o {}kg'.format (maior))
print('O menor peso foi o {}kg'.format (menor))

# Vai dizer qual o maior peso e qual o maior peso , tive duvidas na logica mas deu certo
