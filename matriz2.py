def elementos_repetidos(matriz):
    # Analisando o número de linhas e de colunas da matriz
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])

    # Criando uma lista para armazenar todos os valores da matriz
    lista = []
    for c in range(0, n_linhas):
        for i in range(0, n_colunas):
            lista.append(matriz[c][i])

    # Modificando a lista para pôr os 0's nos números repetidos
    for c in range(0, len(lista)):
        termo = lista[c]
        for i in range((c + 1), len(lista)):
            if lista[i] == termo:
                lista[i] = 0
            else:
                lista[i] = int(lista[i])


    # Repondo os valores da lista na matriz 
    matriz = []
    contador = 0
    for c in range(0, n_linhas):
        linhazinha = []
        for i in range(0, n_colunas):
            linhazinha.append(lista[contador])
            contador += 1
        matriz.append(linhazinha)

    return matriz
