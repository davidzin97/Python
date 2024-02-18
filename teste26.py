numero = int(input('Escolha o numero '))
cont = 0
valor = 0

while True:
    cont += 1
    valor += numero
    numero = int(input('Escolha o numero: '))
    if numero == 999:
        break

print("Quantidade de números digitados:", cont)
print("Soma dos números digitados:", valor) 

# Usando while e break para fazer o exercicio 