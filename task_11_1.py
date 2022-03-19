class Data:
    def __init__(self, data: str) -> None:
        self.data = data

    @classmethod
    def Type_number(cls, data) -> list:
        """Преобразовывает день-месяц-год к типу Число"""
        try:
            return list(map(int, data.split('-')))
        except:
            raise ValueError('Указана неверная дата')

    @staticmethod
    def is_data_valid(data: str) -> bool:
        """Валидация введеной даты"""
        day: int
        month: int
        year: int

        day, month, year = Data.Type_number(data)

        if not 1 <= day <= 31:
            return False
        if not 1 <= month <= 12:
            return False
        if month in [4, 6, 9, 11] and day == 31:
            return False
        if month == 2 and day == 30:
            return False
        if month == 2 and day == 31:
            return False
        if not year >= 0:
            return False
        return True


if __name__ == '__main__':
    print(Data.Type_number('07-06-1891'))
    print(Data.is_data_valid('06-03-2022'))
    print(Data.Type_number('30-02-2022'))
    print(Data.is_data_valid('31-02-2022'))
    print(Data.Type_number('31-04-2022'))
   # print(Data.is_data_valid('28.02.2022'))

