class Warehouse:
    def __init__(self):
        self._dict = {}

    def add_to_dict(self, Office_equipment):
        """Добавляем в словарь обьект по его названию, в значении будет
        список экземпляров этого оборудования"""
        self._dict.setdefault(Office_equipment.group_name, []).append(Office_equipment)


class Office_equipment:
    def __init__(self, *args):
        super().__init__(*args)
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def input_data(self):
        try:
            global name, make, year, quantity
            name = input(f'Введите название: ')
            make = input(f'Изготовлено в : ')
            year = int(input(f'Год: '))
            quantity = int(input(f'Количество: '))
        except ValueError:
            raise f'Введены некорректные данные'


class Printer(Office_equipment):

    def action(self):
        return f'print'


class Scaner(Office_equipment):

    def action(self):
        return f'scan'


class Xerox(Office_equipment):

    def action(self):
        return f'make copy'


if __name__ == '__main__':
    warehouse = Warehouse()
    printer = Printer()
    scaner = Scaner()
    xerox = Xerox()
    printer.input_data()
    scaner.input_data()
    warehouse.add_to_dict(printer)
    warehouse.add_to_dict(scaner)
    print(warehouse._dict)
