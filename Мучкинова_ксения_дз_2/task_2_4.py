def convert_name_extract(list_in: list) -> list:
    i = 0
    id = 0
    ix = 2
    list_names = []
    for el in list_in:
        el = list_in[i].split().pop()
        list_names.append(el)
        list_names.insert(id, 'Привет, ')
        list_names.insert(ix, '! ')
        i += 1
        id += 3
        ix += 3
    list_out = (('').join(list_names).lower().title())
    return list_out

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй','директор аэлита']
result = convert_name_extract(my_list)
print(result)
