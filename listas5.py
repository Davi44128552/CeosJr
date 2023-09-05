# Importando o módulo time
import time

# Início da contagem do tempo
tempo_inicial = time.time()

# Lista qualquer e análise do número de termos
lista = [24, 56, 12, 78, 43, 89, 31, 67, 15, 50]
n_termos = len(lista)

# Insertion sort da lista
for j in range(1, n_termos):
    x = lista[j]
    i = j - 1

    while i >= 0 and x < lista[i]:
        lista[i + 1] = lista[i]
        i -= 1

    lista[i + 1] = x

# Análise do terceiro maior número
maior3 = lista[-3]
print(f"O terceiro maior termo da lista é igual a {maior3}")

# Fim da contagem de tempo
tempo_final = time.time()
tempo_total = tempo_final - tempo_inicial

print(f"O tempo de processo foi de {tempo_total}, {tempo_inicial}, {tempo_final}")