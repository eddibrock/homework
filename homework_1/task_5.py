#
def get_multiply(primes) -> int:
    """
        Функция для перемножения элементов списка.

    :param primes:
    :return:
    """
    mult_result = 1
    for number in primes:
        mult_result *= number
    return mult_result


def count_find_num(primes) -> list:
    """
        Функция для получения произведений множителей primes, которые меньше limit.

    :param primes:
    :param limit:
    :return:
    """
    limit = 500
    result = set()
    multiply = get_multiply(primes)  # В начале перемножить числа входного списка
    for number in primes:
        mult_result = multiply
        while mult_result < limit:
            result.add(mult_result)
            mult_result *= number
        else:
            continue

    return [len(result), max(result)]


def main():

    primes = [
        [2, 5, 7]
    ]

    for numbers in primes:
        print(count_find_num(numbers))


main()
