from datetime import date

print('')
print('\33[33m-='*20)
print('\33[36mSaiba qual é a categoria do atleta:')
print('\33[33m-='*20)
print('')

a = int(input('\33[33mDigite o ano de nascimento do atleta: '))
print('')
d = date.today().year
idade = d-a 
print('\33[36mO(a) atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('\33[33mEle(a) é classificado(a) como: mirim!')
elif idade <= 14:
    print('\33[33mEle(a) é classificado(a) como: infantil!')
elif idade <= 19:
    print('\33[33mEle(a) é classificado(a) como: junior!')
elif idade <= 25:
    print('\33[33mEle(a) é classificado(a) como: sênior!')
elif idade > 25:
    print('\33[33mEle(a) é classificado(a) como: master!')
print('\33[0m')

# esse exercicio peguei a resposta pq nao sabia como importar a data para o python !
