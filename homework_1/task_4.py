import random


def replace_symbols(idx_list, word, with_symbol) -> str:
    """
        Функция для замены символов в слове по индексам на переданный with_symbol

    :param idx_list:
    :param word:
    :param with_symbol:
    :return:
    """
    word = list(word)
    for idx in idx_list:
        word[idx] = with_symbol

    return ''.join(word)


def banana(search_word, word) -> set:
    """
        Функция для получения множества одинаковых слов из переданного набора букв

    :param search_word:
    :param word:
    :return:
    """
    result = set()

    if len(word) == len(search_word):
        if word == search_word:
            result.add(word)
        return result

    limit = 1000  # Остановить цикл на N итерации
    count = 0
    symbol_len = len(word) - len(search_word)  # Сколько лишних символов в наборе букв
    idx_list = list(range(0, len(word)))  # Список индексов

    while count <= limit:
        rnd_idx = random.sample(idx_list, symbol_len)  # Какие буквы будут заменены на "-"
        replaced_word = replace_symbols(rnd_idx, word, '-')  # Слово с замененными символами
        whole_word = replaced_word.replace('-', '')  # Слово без лишних символов
        if whole_word == search_word:  # Если слово без лишних символов равно искомому - добавить в результат
            result.add(replaced_word)
        count += 1

    return result


def main():
    search_word = 'banana'

    words = [
        'banann',
        'banana',
        'bbananana',
        'bananaaa',
        'bananana',
    ]

    for word in words:
        print(banana(search_word, word))


main()
