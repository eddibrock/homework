def calc_fact(number) -> int:
    """
        Функция для вычисления факториала

    :param number:
    :return:
    """
    mult_result = 1
    for i in range(1, number + 1):
        mult_result *= i

    return mult_result


def zeros(number) -> int:
    """
        Функция для вычисления количества нулей в конце числа

    :param number:
    :return:
    """
    fact_number = str(calc_fact(number))
    how_many_zeros = len(fact_number) - len(fact_number.rstrip('0'))

    return how_many_zeros


def main():
    numbers = [
        0, 6, 30
    ]

    for number in numbers:
        print(zeros(number))


main()
