def expressoes_matematicas():
    a = 10 + 20 * 30
    b = 42 / 30
    c = ((9**4) + 2) * 6 - 1

    result = f"""10 + 20 × 30 = {a}
42 ÷ 30 = {b:.2f}
(9⁴ + 2) × 6 - 1 = {c}
"""
    print(result)


expressoes_matematicas()
