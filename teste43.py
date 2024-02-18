aluno = dict()
aluno ['nome'] = str(input(f"Nome: "))
aluno ['media'] = float(input(f'qual foi a media do {aluno["nome"]}: '))

if aluno['media'] >= 7 :
    aluno ['situaçao'] = 'aprovado'
elif 5 <= aluno['media'] <7 :
    aluno['situaçao'] = 'recuperaçao'
else:
    aluno [ 'situaçao'] = 'reprovado'

print('--' *30)

for k , v in aluno.items():
    print(f'-{k} é igual a {v}')