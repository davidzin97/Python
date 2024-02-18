nota1 = float(input ('Qual foi a primeira nota ?'))
nota2 = float(input ('Qual foi a segunda nota ?'))
res = float((nota1 + nota2) / 2)
print('Média ',res)

if res < 4.99:
    print('Reprovado') 
elif res < 6.9:
    print('Recuperação')
else: 
    print('Aprovado')

    # Media dos alunos com Condiçao