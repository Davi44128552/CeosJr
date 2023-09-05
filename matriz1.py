# Criação da função
def leitor_matriz(doc):
    # Ler o arquivo 
    with open(f"{doc}.txt", "r") as arquivo:
        teste = arquivo.read()

        # Adicionar os valores inteiros a uma lista
        lista = []
        for c in teste:
            if c in ' ,[]':
                continue
            else:
                lista.append(int(c))
        
        # Analisar o arquivo pra tranformar em uma matriz
            # Análise do nº de linhas
        contador_linhas = 0
        for c in teste:
            if c == '[':
                contador_linhas += 1
        contador_linhas -= 1

            # Análise do nº de colunas
        termos_matriz = 0
        for c in teste:
            if c in ' ,[]':
                continue
            else:
                termos_matriz += 1
        contador_colunas = int(termos_matriz / contador_linhas)
        

        # Transformar a lista em matriz
        matriz = []
        contador = 0
        for c in range(0, contador_linhas):
            linhazinha = []
            for i in range(0, contador_colunas):
                linhazinha.append(lista[contador])
                contador += 1
            matriz.append(linhazinha)

        # Retornando a matriz
        return matriz
    
teste = leitor_matriz("matrizinha")