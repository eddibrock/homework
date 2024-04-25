def domain_name(url, substr) -> str:
    """
        Функция для получения доменного имени из url адреса

    :param url:
    :param substr:
    :return:
    """
    substrw = substr + 'www.'
    if substrw in url:
        domain = url.replace(substrw, '').split('.')[0]
    else:
        domain = url.replace(substr, '').split('.')[0]

    return domain


def main():
    urls = [
        "http://github.com/carbonfive/raygun",
        "http://www.zombie-bites.com",
        "https://www.cnet.com",
        "http://google.com",
        "http://google.co.jp",
        "www.xakep.ru",
        "https://youtube.com",
        "https://youtubewww.com",
        "http://hgoogle.com",
    ]

    for url in urls:
        if 'https://' in url:
            print(domain_name(url, 'https://'))
        elif 'http://' in url:
            print(domain_name(url, 'http://'))


main()
