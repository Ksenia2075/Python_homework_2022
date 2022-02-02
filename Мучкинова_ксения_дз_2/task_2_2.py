def convert_list_in_str(list_in: list) -> str:
    list_out = []
    i = 0
    for elem in list_in:
        if elem.isdigit():
            list_out.append('"')
            list_out.append(elem.zfill(2))
            list_out.append('"')
        elif elem[0] == '+' and elem[1].isdigit():
            list_out.append('"')
            list_out.append(elem.zfill(3))
            list_out.append('"')
        elif elem[0] == '-' and elem[1].isdigit():
            list_out.append('"')
            list_out.append(elem.zfill(3))
            list_out.append('"')
        elif elem.isalpha():
            list_out.append(elem)
        str_out = (' ').join(list_out)
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
