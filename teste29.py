masculino = 0
feminino = 0
idade20 = 0

while True:
    idade = int(input('Quantos anos a pessoa tem? '))
    sexo = input('Qual o sexo [M][F] ? ').upper()

    if idade >= 20 and sexo == 'F':
        idade20 += 1
    
    if sexo == 'M':
        masculino += 1
    elif sexo == 'F':
        feminino += 1
    else:
        print('Sexo não reconhecido. Tente novamente.')
        continue
    
    conti = input('Deseja continuar [S][N]? ').upper()
    if conti == 'N':
        break

print('São {} pessoas do sexo Masculino'.format(masculino))
print('São {} pessoas do sexo Feminino'.format(feminino))
print('São {} garotas com 20 anos ou mais'.format(idade20))

# cadastro de pessoas com estrutura de repitiçao 
