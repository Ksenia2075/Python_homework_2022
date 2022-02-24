import re


def email_parse(email: str) -> dict:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    RE_MAIL = re.compile(r'(?P<username>([A-Za_z0-9]+[.-_])*[A-Za-z0-9]+)@(?P<domain>[A-Za-z0-9]+(\.[A-Z|a-z]{2,})+)')
    try:
        test_email = list(map(lambda x: x.groupdict(), RE_MAIL.finditer(email)))
        print(test_email[0])
    except:
        raise ValueError


if __name__ == '__main__':
    email_parse('someone@geekbrains.ru')
    #email_parse('someone@geekbrainsru')