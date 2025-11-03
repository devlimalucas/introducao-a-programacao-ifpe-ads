A = []
test = [1, 0, 5, -2, -5, 7]


def take_number():
    number = int(input("Digite um número: "))
    A.append(number)


def show_numbers_in_list(lista):
    for i in range(len(lista)):
        print(f"Posição atual: {i} - Valor: {lista[i]}")


def modificando_listas():
    print("Adicione a lista com 6 números")

    for i in range(6):
        take_number()

    print(f"Lista: {A}")

    sumPositions = sum([A[0], A[1], A[5]])

    print(f"A soma das posições 0, 1 e 5 é: {sumPositions}")

    A[4] = 100

    show_numbers_in_list(A)


modificando_listas()
