def domain_name(url) -> str:
    """
        Функция для получения доменного имени из url адреса

    :param url:
    :return:
    """
    domain = url.lstrip('htpsw:/.').split('.')[0]
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

        "http://hgoogle.com"
    ]

    for url in urls:
        print(domain_name(url))


main()
