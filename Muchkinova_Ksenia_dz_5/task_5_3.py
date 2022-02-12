tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Наталия', 'Андрей']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    """Возвращаем кортеж где счетчик tutors, а элемент klasses.
    Создаем условие при котором, если не хватает елемента, возвращаем None """
    return ((tutors, klasses[i]) if i < len(klasses) else (tutors, None)
            for i, tutors in enumerate(tutors))


generator = check_gen(tutors, klasses)
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))
next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration