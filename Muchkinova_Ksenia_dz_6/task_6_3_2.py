import sys
import json


def zip_func(a_list, b_list):
    #получаем кортежи элементов из двух списков
    return ((a_elem, b_list[i]) if i < len(b_list) else (a_elem, None)
            for i, a_elem in enumerate(a_list))

def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """

    with open('users.csv', 'r', encoding='utf-8') as f1:   #открываем файл для чтения в кодировке utf-8
        key_file = f1.readlines()                          #считываем файл в список
        key_file = [line.rstrip() for line in key_file]    #убираем знаки в конце строки

    with open('hobby.csv','r', encoding='utf-8') as f2:
        value_file = f2.readlines()
        value_file = [line.rstrip() for line in value_file]

    if len(key_file) < len(value_file):     #если длина файла в котором будут ключи меньше длины файла в котором будут значения
        sys.exit(1)                         #выходим из программы с кодом 1

    else:                                   #иначе
        dict_out = {}                       #создаем пустой словарь
        for key, value in zip_func(key_file, value_file):  #запускаем цикл для элементов кортежа созданного из двух списков
            dict_out[key] = value if value else None  #ключ в словаре это первый элемент, к нему присваеваем значение второго элемента,
                                                      # если не хватает второго элемента, присваеваем значение None
    return dict_out        #возвращаем словарь


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)