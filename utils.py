def take_number():
    return int(input("Digite um número: "))


def take_number_in_range(rangeNumber):
    numbers = []

    for i in range(rangeNumber):
        number = take_number()
        numbers.append(number)

    return numbers


def quadrado_da_lista(lista):
    numbers = []

    for i in range(len(lista)):
        numbers.append(lista[i] ** lista[i])

    return numbers
