somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
totdemulher20 = 0
for p in range(1,5):
    print ('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('sexo [M/F]: ')).strip()
    somaidade +=idade
    if p == 1 and sexo in 'Mm' :
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totdemulher20 += 1 
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homen mais velho tem {} anos e se chama {}'.format(maioridadehomen, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totdemulher20))