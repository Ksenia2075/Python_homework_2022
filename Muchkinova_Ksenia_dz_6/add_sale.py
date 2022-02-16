with open('bakery.csv', mode='a', newline='', encoding='utf-8') as fw:
    number = input('Введите число:')
    fw.write(f'{number}\n')