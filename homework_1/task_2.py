def int32_to_ip(int32) -> str:
    """
        Функция для получения IPv4 адреса

    :param int32:
    :return:
    """
    result = []
    for i in int32.to_bytes(4, byteorder='big', signed=False):
        result.append(str(i))
    return '.'.join(result)


def main():
    numbers = [
        2149583361,
        32,
        0,
        2154959208,
        2149583361,
    ]

    for number in numbers:
        print(int32_to_ip(number))


main()
