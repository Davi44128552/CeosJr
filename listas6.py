# Importando o módulo time
import time

# Início da contagem do tempo
tempo_inicial = time.time()

# As listas que serão manipuladas
lista1 = []
lista2 = []

# Criação de uma lista para todos os termos das duas listas
# e a contagem do número de termos total
lista_soma = lista1 + lista2
n_termos = len(lista_soma)

# Aplicação do insertion sort (Para organizar a lista, para adicionar depois nas outras duas listas)
for j in range(1, n_termos):
    x = lista_soma[j]
    i = j - 1

    while i >= 0 and x < lista_soma[i]:
        lista_soma[i + 1] = lista_soma[i]
        i -= 1

    lista_soma[i + 1] = x

# A redefinição das listas, agora como vazias
lista1 = []
lista2 = []

# Adição dos valores nas listas (Os n_termo / 2 primeiros da lista_soma serão da lista1 e o resto da 2)
metade_n_termos = int(n_termos / 2)

for c in range(0, metade_n_termos):
    lista1.append(lista_soma[c])

for c in range(metade_n_termos, n_termos):
    lista2.append(lista_soma[c])

# Saída das listas
print(lista1)
print(lista2)

# Fim da contagem de tempo
tempo_final = time.time()
tempo_total = tempo_final - tempo_inicial
print(f"O tempo de processo foi de {tempo_total}")