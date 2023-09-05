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