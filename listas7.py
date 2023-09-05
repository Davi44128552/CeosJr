# As listas e a verificação de seu tamanho
lista1 = []
lista2 = []
n_termos = len(lista1)

# Insertion sort
    # Lista 1
for j in range(1, n_termos):
    x = lista1[j]
    i = j - 1

    while i >= 0 and x < lista1[i]:
        lista1[i + 1] = lista1[i]
        i -= 1

    lista1[i + 1] = x

    # Lista 2
for j in range(1, n_termos):
    x = lista2[j]
    i = j - 1

    while i >= 0 and x < lista2[i]:
        lista2[i + 1] = lista2[i]
        i -= 1

    lista2[i + 1] = x

# Verificação da igualdade das listas
if lista1 == lista2:
    print("A lista 2 é uma permutação da lista 1")

else:
    print("A lista 2 NÃO é uma permutação da lista 1")
