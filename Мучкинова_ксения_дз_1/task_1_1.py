1 задание
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
    
def convert_time(duration: int) -> str:
    if duration < 60:
        res_time = (duration, 'сек')
    elif duration < 3600:
        res_time = (duration // 60, 'мин', duration % 60, 'сек')
    elif duration < 86400:
        res_time = (duration // 3600, 'час', duration % 3600 // 60, 'мин', duration % 3600 % 60, 'сек')
    elif duration < 31536000:
        res_time = (duration // 86400, 'дн', duration % 86400 // 3600, 'час', duration % 86400 % 3600 // 60, 'мин', duration % 86000 % 3600 % 60, 'сек')
    elif duration > 31536000:
        res_time = ('Вы ввели очень большое число')
    return(res_time)
duration = 400153
result = convert_time(duration)
print(result)

2 задание
a) Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

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

3 задание
Реализовать склонение слова процент во фразе N процентов. Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
    
   def transform_sring(number: int) -> str:
    if number % 10 == 0:
        return str(number) + ' процентов'
    elif (number >= 5 and number <= 20):
        return str(number) + ' процентов'
    elif number % 10 == 1 :
        return str(number) + ' процент'
    elif number % 10 <= 4:
        return str(number) + ' процента'
    elif number % 10 <=9:
        return str(number) + ' процентов'

for n in range(1, 101):
    print(transform_sring(n))


