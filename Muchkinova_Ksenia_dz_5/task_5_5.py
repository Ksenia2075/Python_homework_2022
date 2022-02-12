def get_uniq_numbers(src: list):
    gun = set()                            # создаем множество
    for el in src:                         # запускаем цикл перебора элементов
        if el not in gun:                  # если елемента нет во множестве
            gun.add(el)                    # добавляем елемент
        else:                              # если есть
            gun.discard(el)                # удаляем из множества
    return [i for i in src if i in gun]    # возвращаем список перебирая елементы и сравнивая их,
                                           #  если елемент есть в исходном списке и во множестве, то мы его возвращаем

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))