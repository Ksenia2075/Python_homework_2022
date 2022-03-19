class NumbError(Exception):
    def __init__(self):
        self.number_list = []

    def check_is_number(self):
        global user_input
        while True:
            try:
                try:
                    user_input = int(input('Введите число: '))
                    anser = input(f'Добавляем "{user_input}" в список. Хотите продолжить?: ').lower()
                    self.number_list.append(user_input)
                    if anser == 'stop':
                        print(self.number_list)
                        break
                except ValueError:
                    raise NumbError
            except NumbError:
                anser = input(f"Вы ввели не число! Хотите продолжить?: ").lower()
                if anser == 'stop':
                    print(self.number_list)
                    break
                else:
                    self.check_is_number()


if __name__ == '__main__':
    a = NumbError()
    a.check_is_number()

    