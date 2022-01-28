def sum_list_1(dataset: list) -> int:
    del_7 = 0
    for elem in dataset:
        num = 0
        while (elem != 0):
            num = num + elem % 10
            elem = elem // 10
        if num % 7 == 0:
            del_7 =+ dataset[num]
    return del_7

def sum_list_2(dataset: list) -> int:
    del_7 = 0
    for elem in dataset:
        elem = elem + 17
        num = 0
        while (elem != 0):
            num = num + elem % 10
            elem = elem // 10
        if num % 7 == 0:
            del_7 =+ dataset[num]
    return del_7


my_list = [x ** 3 for x in range(1, 1001, 2)]  # список кубов
result_1 = sum_list_1(my_list)
print(result_1)

result_2 = sum_list_2(my_list)
print(result_2)

