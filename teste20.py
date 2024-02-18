from datetime import date
atual = date.today().year

totmaior = 0
totmenor = 0

for pessoa in range(0,7):
    nascimeto = int(input('Qual Ano a {}° Nascimento ? '.format(pessoa)))
    idade = atual - nascimeto
    if idade >= 18 :
        totmaior += 1
    else:
        totmenor += 1

print ('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print ('E também tivemos {} pessoas menores de idade'.format(totmenor))

# Vai dizer quntas pessoas sao de maior e quantas pessoas sao de menor 
#pegando a data atua do PC
