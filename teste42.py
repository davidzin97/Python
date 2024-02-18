# Inicializando variáveis
edia = 0
lista = []
notas = []
nota1 = []
nota2 = []
ficha = []

# Loop principal
while True:
    # Recebendo dados do usuário
    nome = str(input('Digite o nome:'))
    nota1 = float(input('Digite a NOTA 1:'))
    nota2 = float(input('Digite a NOTA 2:'))
    
    # Calculando a média
    media = (nota1 + nota2) / 2

    # Adicionando os dados à lista 'ficha'
    ficha.append([nome, [nota1, nota2], media])

    # Perguntando se o usuário deseja continuar
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Digite "S" para continuar ou "N" para sair:')).upper().strip()[0]

    if resp == 'N':
        break

# Imprimindo a tabela com os resultados
print('-=' * 15)
print(f'{"No.":<5}{"NOME":<10}{"MÉDIA":>8}')
print('_' * 30)

for i, a in enumerate(ficha):
    print(f'{i + 1:<5}{a[0]:<10}{a[2]:>8}')


# codigo que ve as medias e cria uma tabela codigo todo explicado com comentarios para relembrar 