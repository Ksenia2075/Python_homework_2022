class Stationery:
    title: str

    def __init__(self, title: str) -> None:
        self.title = title

    def draw(self) -> None:
        print(f'Запуск отрисовки')


# определите классы ниже согласно условий задания
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(self)
        self.title = 'Ручка'

    def draw(self) -> None:
        print(f'{self.title} приступил к отрисовке обьекта {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(self)
        self.title = 'Карандаш'

    def draw(self) -> None:
        print(f'Запуск отрисовки')
        print(f'{self.title} приступил к отрисовке обьекта {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(self)
        self.title = 'Маркер'

    def draw(self) -> None:
        print(f'{self.title} приступил к отрисовке обьекта {self.title}')


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()  # Pen: приступил к отрисовке объекта "Ручка"
    handle.draw()  # Handle: приступил к отрисовке объекта "Маркер"
    pencil.draw()  # Пример вывода ниже в многострочном комментарии
    """
    Запуск отрисовки
    Pencil: приступил к отрисовке объекта "Карандаш"
    """