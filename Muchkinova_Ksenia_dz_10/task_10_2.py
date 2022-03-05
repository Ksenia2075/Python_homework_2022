from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param: float):
        self.param = param

    @abstractmethod
    def calculate(self): ...

    @property
    def calculate(self):
        #общий расход ткани
        return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5} + {2 * self.param + 0.3 :.2f}'


class Coat(Clothes):
    @property
    def calculate(self):
        return f'Для пошива пальто необходимо: {self.param / 6.5 + 0.5 :.2f} ткани'


class Costume(Clothes):
    @property
    def calculate(self):
        return f'Для пошива костюма необходимо: {2 * self.param + 0.3 :.2f} ткани'


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3