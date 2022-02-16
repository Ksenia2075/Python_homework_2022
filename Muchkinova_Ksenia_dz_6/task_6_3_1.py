import csv


def csv_writer(list_f, csv_file):
    #записываем list_f в csv_file
    with open(csv_file, mode='w', newline='', encoding='utf-8') as w_file:   #создаем файл csv для записи в кодировке utf-8
        w_file = csv.writer(w_file)     #записываем в файл
        for line in list_f:           #начинаем цикл записи
         w_file.writerow(line)       #в файл записывается строка из переданного списка


if __name__ == "__main__":
    #создаем первый список и разделяем как нам надо
    users_list = ['Иванов Иван Иванович'.split(' '),
                  'Петров Петр Петрович'.split(' '),
                  'Сергеев Сергей Сергеевич'.split(' ')]

    csv_file_1 = 'users.csv'                #присваеваем переменной название csv файла
    csv_writer(users_list, csv_file_1)      #передаем в созданную функцию список и название файла, создаем csv файл

    # создаем второй список и разделяем как нам надо
    hobby_list = ['скалолазание, охота'.split(','),
                  'горные лыжи'.split(','),
                  'дайвинг, яхтинг'.split(',')]

    csv_file_2 = 'hobby.csv'                 #присваеваем переменной название csv файла
    csv_writer(hobby_list, csv_file_2)       #передаем в созданную функцию список и название файла, создаем csv файл