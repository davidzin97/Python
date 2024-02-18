lista1  = [[],[],[]]
lista2  = [[],[],[]]
lista3  = [[],[],[]]

lista1[0].append(int(input('numero na posiçao 0,0 ' )))
lista1[1].append(int(input('numero na posiçao 0,1 ' )))
lista1[2].append(int(input('numero na posiçao 0,2 ' )))

lista2[0].append(int(input('numero na posiçao 1,0 ' )))
lista2[1].append(int(input('numero na posiçao 1,1 ' )))
lista2[2].append(int(input('numero na posiçao 1,2 ' )))

lista3[0].append(int(input('numero na posiçao 2,0 ' )))
lista3[1].append(int(input('numero na posiçao 2,1 ' )))
lista3[2].append(int(input('numero na posiçao 2,2 ' )))

print(lista1)
print(lista2)
print(lista3)

# criando uma matriz usando listas


"""" 
def preencher_matriz():
    matriz = [[0, 0, 0] for _ in range(3)]  # Inicializa uma matriz 3x3 com zeros
    
    for i in range(3):
        for j in range(3):
            matriz[i][j] = int(input(f'Número na posição {i},{j}: '))
    
    return matriz

# Preencher as três matrizes
lista1 = preencher_matriz()
lista2 = preencher_matriz()
lista3 = preencher_matriz()

# Imprimir as matrizes
print(lista1)
print(lista2)
print(lista3)
"""

# aqui uma forma mais simples de fazer o codigo