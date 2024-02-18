galera = list()
totmai = totmen = 0

for c in range(0, 3):
    dado = list()  # Inicialize 'dado' dentro do loop
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))  # Converta a idade para um número inteiro
    galera.append(dado[:])

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')

# usa o input pra coloca dados dentro de uma lista em um looping