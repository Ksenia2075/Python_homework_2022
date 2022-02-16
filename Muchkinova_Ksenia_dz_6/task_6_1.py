from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    for _ in line:
        remote_addr = line.split('- -')[0]              #разбиваем строку по знаку ('- -') и получаем первый атрибут под индексом [0]
        type_and_resource = line.split('"')[1]          #рабиваем строку по знаку ('"') и берем (уже ставшимн вторым) необходимый нам элемент под индексом [1]
        request_type = type_and_resource.split()[0]     #разбиваем взятый элемент и получаем второй атрибут под индексом [0]
        requested_resource = type_and_resource.split()[1] #разбиваем взятый элемент и получаем третий атрибут под индексом [1]
        return (remote_addr, request_type, requested_resource)  #возвращаем кортеж атрибутов


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:   #открываем файл для чтения в кодировке utf-8 как fr
    for line in fr:                                         #запускаем цикл чтения
        list_out.append(get_parse_attrs(fr.readline()))     #построчно считываем файл, через функцию парсируем строку и добавляем кортеж атрибутов в list_out

pprint(list_out)