
valor_sacado = int(input("Digite o valor a ser sacado: R$"))


cédulas_de_50 = 0
cédulas_de_20 = 0
cédulas_de_10 = 0
cédulas_de_1 = 0


while valor_sacado > 0:
    if valor_sacado >= 50:
        cédulas_de_50 += 1
        valor_sacado -= 50
    elif valor_sacado >= 20:
        cédulas_de_20 += 1
        valor_sacado -= 20
    elif valor_sacado >= 10:
        cédulas_de_10 += 1
        valor_sacado -= 10
    else:
        cédulas_de_1 += valor_sacado
        valor_sacado = 0


print(f"Cédulas de R$50: {cédulas_de_50}")
print(f"Cédulas de R$20: {cédulas_de_20}")
print(f"Cédulas de R$10: {cédulas_de_10}")
print(f"Cédulas de R$1: {cédulas_de_1}")

# progama de caixa eltronico tive duvidas com a logica