def take_number():
    return int(input("Digite um número: "))


def cal_expressao():
    print("Calcular a soma de três números")

    acc = 0

    for i in range(3):
        value = take_number()
        acc += value

    print(f"A suma dos números é: {acc}")


cal_expressao()
