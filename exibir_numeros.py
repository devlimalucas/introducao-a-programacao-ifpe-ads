from utils import take_number


def exibir_numeros():
    numbers = []

    for i in range(6):
        number = take_number()
        numbers.append(number)

    print(f"Número digitatos: {numbers}")


exibir_numeros()
