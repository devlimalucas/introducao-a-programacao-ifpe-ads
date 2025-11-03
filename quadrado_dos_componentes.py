from utils import take_number_in_range
from utils import quadrado_da_lista


def quadrado_dos_compomnentes():
    numbers = take_number_in_range(10)

    numbers_squadred = quadrado_da_lista(numbers)

    print(numbers)
    print(numbers_squadred)


quadrado_dos_compomnentes()
