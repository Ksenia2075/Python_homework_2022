def thesaurus(*args) -> dict:
    #создает словарь, где первая буква слова ключ
    dict_out = {}
    for name in args:
        if dict_out.get(name[0]):
            dict_out[name[0]].append(name)
        else:
            dict_out[name[0]] = [name]
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Andrew", "Jack"))
