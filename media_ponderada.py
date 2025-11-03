primeira_nota = float(input("Digite a primeira nota: "))
peso_primeira_nota = float(input("Digite o peso da segunda nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
peso_segunda_peso = float(input("Digite o peso da segunda nota: "))


def media_ponderada():
    calc_primeira_nota = primeira_nota * peso_primeira_nota
    calc_segunda_nota = segunda_nota * peso_primeira_nota
    print((calc_primeira_nota + calc_segunda_nota) /
          (peso_primeira_nota + peso_segunda_peso))


media_ponderada()
