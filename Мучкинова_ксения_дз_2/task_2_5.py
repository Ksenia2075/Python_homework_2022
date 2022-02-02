from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    list_out = []
    end_word: str = ", "
    for elem, num in enumerate(list_in):
        price_list = str(f"{float(num):.2f}").split(".")
        if elem == len(list_in) - 1:
            end_word = "\n"
        price = str((f"{price_list[0]} руб {price_list[1]} коп"))
        list_out.append(price)
        str_out = (', ').join(list_out)
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    list_in.sort()
    return list_in


print(id(my_list))
result_2 = sort_prices(my_list)
print(id(result_2))
print(result_2)


def sort_price_adv(list_in: list) -> list:
    list_out = []
    copy_list = list(list_in.copy())
    copy_list.sort()
    copy_list.reverse()
    list_out.append(copy_list)
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    list_out = []
    list_in.sort()
    list_out = list_in[-6:-1]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
