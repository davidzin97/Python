


masculino = ''
feminino = ''
sexo = input('Qual o Sexo [M][F] ?').upper()

if sexo == 'M':
    masculino = sexo
elif sexo == 'F':
    sexo = feminino
else :
    sexo = input('Qual o Sexo [M][F] ?').upper()
print(sexo)