def zeros(number) -> int:
    """
        Функция для вычисления количества нулей в конце числа

    :param number:
    :return:
    """
    result = 0
    while number > 4:
        result += number // 5
        number //= 5
    return result


def main():
    numbers = [
        0, 6, 30
    ]

    for number in numbers:
        print(zeros(number))


main()
