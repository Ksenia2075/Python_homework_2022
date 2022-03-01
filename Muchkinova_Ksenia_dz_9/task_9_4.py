from inspect import Traceback


class Car:
    is_police: bool = False

    def __init__(self, speed: int, colour: str, name: str):
        """
        Конструктор класса
        :param speed: текущая скорость автомобиля
        :param color: цвет автомобиля
        :param name: название марки автомобиля
        """
        self.speed = speed
        self.colour = colour
        self.name = name

    def go(self) -> None:
        """
        Увеличивает значение скорости на 15
        :return: в stdout сообщение по формату
            'Машина <название марки машины> повысила скорость на 15: <текущая скорость машины>'
        """
        self.speed = self.speed + 15
        print(f'{self.name} повысила скорость на 15: {self.speed}')
        return f'{self.name} повысила скорость на 15: {self.speed}'

    def stop(self) -> None:
        """
        При вызове метода скорость становится равной '0'
        :return: в stdout сообщение по формату '<название марки машины>: остановилась'
        """
        self.speed = 0
        print(f'{self.name}: остановилась')
        return f'{self.name}: остановилась'

    def turn(self, direction: str) -> None:
        """
        Принимает направление движения автомобиля
        :param direction: строковое представление направления движения, может принимать только
            следующие значения: 'направо', 'налево', 'прямо', 'назад'
        :return: в stdout сообщение по формату
            '<название марки машины>: движется <direction>'
        """
        if direction == 'направо':
            print(f'{self.name}: движется {direction}')
          # return f'{self.name}: движется {direction}
        elif direction == 'налево':
            print(f'{self.name}: движется {direction}')
            # return f'{self.name}: движется {direction}
        elif direction == 'прямо':
            print(f'{self.name}: движется {direction}')
            # return f'{self.name}: движется {direction}
        elif direction == 'назад':
            print(f'{self.name}: движется {direction}')
            # return f'{self.name}: движется {direction}
        else:
            print('ValueError: нераспознанное направление движения')


    def show_speed(self) -> None:
        """
        Проверка текущей скорости автомобиля
        :return: в stdout выводит сообщение формата
            '<название марки машины>: текущая скорость <значение текущей скорости> км/час'
        """
        print(f'{self.name}: текущая скорость {self.speed} км/ч')
        return f'{self.name}: текущая скорость {self.speed} км/ч'


# определите классы TownCar, WorkCar, SportCar, PoliceCar согласно условия задания
class TownCar(Car):
    def show_speed(self) -> None:
        if self.speed > 60:
            print(f'Alarm!!! Speed!!!')
            return f'Alarm!!! Speed!!!'
        else:
            print(f'{self.name}: текущая скорость {self.speed} км/ч')
            return f'{self.name}: текущая скорость {self.speed} км/ч'


class WorkCar(Car):
    def show_speed(self) -> None:
        if self.speed > 40:
            print(f'Alarm!!! Speed!!!')
            return f'Alarm!!! Speed!!!'
        else:
            print(f'{self.name}: текущая скорость {self.speed} км/ч')
            return f'{self.name}: текущая скорость {self.speed} км/ч'


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True
    def show_speed(self) -> None:
        print(f'{self.name}: текущая скорость {self.speed} км/ч')
        print(f'Вруби мигалку и забудь про скорость!')
        return f'{self.name}: текущая скорость {self.speed} км/ч'
        return f'Вруби мигалку и забудь про скорость!'


if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, "blue", 'BMW')
    sport_car = SportCar(300, 'white', 'Ferrari')
    town_car.go()  # Машина WW_Golf повысила скорость на 15: 56
    town_car.show_speed()  # WW_Golf: текущая скорость 56 км/час
    work_car.show_speed()  # Alarm!!! Speed!!!
    town_car.stop()  # WW_Golf: остановилась
    police_car.show_speed()
    # BMW: текущая скорость 120 км/час
    # Вруби мигалку и забудь про скорость!
    sport_car.turn('назад')  # Ferrari(SportCar): движется назад
    sport_car.turn('right')
    """
    Traceback (most recent call last):
      ...
    ValueError: нераспознанное направление движения
    """



