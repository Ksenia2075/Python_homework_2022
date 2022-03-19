class Warehouse:
    def __init__(self):
        self._dict = {}

    def add_to_dict(self, office_equipment):
        """Добавляем в словарь обьект по его названию, в значении будет
        список экземпляров этого оборудования"""
        self._dict.setdefault(office_equipment.group_name, []).append(office_equipment)


class Office_equipment:
    def __init__(self, name, make, year, quantity):
        self.name = name
        self.make = make
        self.year = year
        self.quantity = quantity
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __str__(self):
        return f'Добавляем на склад:\n Модель: {self.name} \n страна изготовитель: {self.make} \n год выпуска: {self.year} \n количество: {self.quantity}'


class Printer(Office_equipment):
    def __init__(self, name, make, year, quantity, type_of_printer):
        super().__init__(name, make, year, quantity)
        self.type_of_printer = type_of_printer

    def type_name(self):
        return f'{self.type_of_printer}'


class Scaner(Office_equipment):
    def __init__(self, name, make, year, quantity, type_of_scaner):
        super().__init__(name, make, year, quantity)
        self.type_of_scaner = type_of_scaner

    def type_name(self):
        return f'{self.type_of_scaner}'


class Xerox(Office_equipment):
    def __init__(self, name, make, year, quantity, type_of_xerox):
        super().__init__(name, make, year, quantity)
        self.type_of_xerox = type_of_xerox

    def type_name(self):
        return f'{self.type_of_xerox}'


if __name__ == '__main__':
    warehouse = Warehouse()
    printer = Printer('Canon', 'Japan', 2020, 5, 'лазерный')
    scaner = Scaner('HP', 'China', 2018, 3, 'планшетный')
    xerox = Xerox('Xerox', 'China', 2021, 6, 'черно-белый')
    warehouse.add_to_dict(printer)
    warehouse.add_to_dict(scaner)
    warehouse.add_to_dict(xerox)

    print(warehouse._dict)
    print(printer.__str__())
    print(printer.type_name())



