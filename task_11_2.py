from sys import exit


class Div_error(Exception):
    def __init__(self, *args) -> None:
        super().__init__(*args)

    def divnum(self):
        try:
            a = float(input('Введите делимое: '))
            b = float(input('Введите делитель: '))
        except:
            print('Допустимо введение только числа')
            exit(1)
        try:
            if b == 0:
                raise Div_error('На 0 делить нельзя!')
            else:
                result = a / b
                print(result)
        except Div_error as exit_1:
            print(exit_1)


if __name__ == '__main__':
    a = Div_error()
    a.divnum()

