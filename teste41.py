import random, time

num = int(input('Quantas vezes voce quer apostar ? '))

for i in range(0, num):

    print(f'Numero da aposta {i+1}:', end=" ")

    aposta = random.sample(range(1, 26), 15)

    print(sorted(aposta))

    time.sleep(2)

    # progama que gera numeros para a Loto facil