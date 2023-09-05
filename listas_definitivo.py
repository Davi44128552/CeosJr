# Abertura
print("\033[1;35m=\033[m" * 10, "\033[1;33mMANIPULADOR DE LISTAS\033[m", "\033[1;35m=\033[m" * 10)
print("\033[4mDesenvolvido por Davi Iury\033[m")

# Opções
print("Qual exercício você gostaria de ver?")
escolha = int(input(" [ 1 ] Exercício 5 \n [ 2 ] Exercício 6 \n [ 3 ] Exercício 7 \n"))

if escolha == 1:
    # Introdução
    lista = []
    termos = int(input("Digite o número de termos que você deseja adicionar à lista: "))

    # Criação da lista pelo usuário
    for c in range(0, termos):
        num = float(input(f"Digite o {c + 1}º termo: "))
        lista.append(num)

    # Insertion sort da lista
    for j in range(1, termos):
        x = lista[j]
        i = j - 1

        while i >= 0 and x < lista[i]:
            lista[i + 1] = lista[i]
            i -= 1

        lista[i + 1] = x

    # Análise do terceiro maior número
    maior3 = lista[-termos]
    print(f"O terceiro maior termo da lista é igual a {maior3}")

elif escolha == 2:
    # Introdução
    lista1 = []
    lista2 = []
    termos = int(input("Digite o número de termos que você deseja adicionar às listas: "))

    # Criação das listas pelos usuários
        # Lista 1
    for c in range(0, termos):
        num = float(input(f"Digite o {c + 1}º termo da lista 1: "))
        lista1.append(num)

        # Lista 2
    for c in range(0, termos):
        num = float(input(f"Digite o {c + 1}º termo da lista 2: "))
        lista2.append(num)

    # Criação de lista para todos os termos das duas listas e contagem do número de termos
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

    # Adição dos valores nas listas  
    metade_n_termos = int(n_termos / 2)

    for c in range(0, metade_n_termos):
        lista1.append(lista_soma[c])

    for c in range(metade_n_termos, n_termos):
        lista2.append(lista_soma[c])

    # Saída das listas
    print(lista1)
    print(lista2)

elif escolha == 3:
    # Introdução
    lista1 = []
    lista2 = []
    termos = int(input("Digite o número de termos que você deseja adicionar às listas: "))

    # Criação das listas pelos usuários
        # Lista 1
    for c in range(0, termos):
        num = float(input(f"Digite o {c + 1}º termo da lista 1: "))
        lista1.append(num)

        # Lista 2
    for c in range(0, termos):
        num = float(input(f"Digite o {c + 1}º termo da lista 2: "))
        lista2.append(num)

        # Insertion sort
    # Lista 1
    for j in range(1, termos):
        x = lista1[j]
        i = j - 1

        while i >= 0 and x < lista1[i]:
            lista1[i + 1] = lista1[i]
            i -= 1

        lista1[i + 1] = x

    # Lista 2
    for j in range(1, termos):
        x = lista2[j]
        i = j - 1

        while i >= 0 and x < lista2[i]:
            lista2[i + 1] = lista2[i]
            i -= 1

        lista2[i + 1] = x

    # Verificação da igualdade das listas
    if lista1 == lista2:
        print("\033[32mA lista 2 é uma permutação da lista 1\033[m")

    else:
        print("\033[31mA lista 2 NÃO é uma permutação da lista 1\033[m")
