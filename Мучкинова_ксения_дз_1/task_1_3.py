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
