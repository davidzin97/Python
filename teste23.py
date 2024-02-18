'''r = input('Qual é seu sexo ? ')
if r == 'f' or 'm':
    print('Sexo valido')
    
while r != 'f' or 'm': 
    print('Sexo invalido')
    r = input('Qual é seu sexo ? ')'''

# Fiz um looping muito loko

s = str(input('Por favor, digite o sexo (M ou F): ')).upper().strip()[0]
while s != 'F' and s != 'M': #enqunto s for diferente de F e M 
    s = str(input('Dados inválidos. Por favor, digite o sexo (M ou F): ') # faça dados invalidos e pergunte dnv
            ).upper().strip()[0]
if s == 'F':
    print('Sexo Feminino cadastrado.')
if s == 'M':
    print('Sexo Masculino cadastrado.')

# cadastro masculino ou feminino
