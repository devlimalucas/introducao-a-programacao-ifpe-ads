from utils import take_number_in_range


def maior_e_menor():
    numbers = take_number_in_range(10)

    print(f"O maior número é: {max(numbers)}")
    print(f"O menor número é: {min(numbers)}")


maior_e_menor()
