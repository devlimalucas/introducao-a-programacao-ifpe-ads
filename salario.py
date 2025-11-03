def salario_services(salario, service):
    if (salario == 750 and service == "aumento"):
        print("Calculando aumento de salário")

        result = 750 * 1.15

        print(f"O salário atual é: {result:.2f}")


salario_services(750, "aumento")
