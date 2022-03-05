class Cell:

    def __init__(self, cells: int):
        self.cells = cells

    def check_cells(self, other):
        if not isinstance(other, Cell):
            raise TypeError('действие допустимо только для экземпляров того же класса')

    def make_order(self, number: int) -> str:
        result = ''
        for i in range(self.cells // number):
            result += '*' * number + '\n'
        result += '*' * (self.cells % number) + '\n'
        return result

    def __add__(self, other):
        self.check_cells(other)
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        self.check_cells(other)
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else:
            raise ValueError('недопустимая операция')

    def __mul__(self, other):
        self.check_cells(other)
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        self.check_cells(other)
        return Cell(self.cells // other.cells)

    def __floordiv__(self, other):
        self.check_cells(other)
        return Cell(self.cells / other.cells)


if __name__ == '__main__':
    cell_1 = Cell(15)
    cell_2 = Cell(10)
    cell_3 = Cell(3)

    print(cell_1.make_order(10))
    """
       **********
       *****
       """

    sum_cell = cell_2 + cell_3
    print(sum_cell.make_order(6))
    """
    ******
    ******
    *
    """

    sub_cell = cell_1 - cell_3
    print(sub_cell.make_order(6))
    """
    ******
    ******
    """

    mul_cell = cell_2 * cell_3
    print(mul_cell.cells)  # 30

    floordiv_cell = cell_2 // cell_3
    print(floordiv_cell.cells)  # 3

    truediv_cell = cell_1 / cell_2
    print(truediv_cell.cells)  # 1

    try:
        cell_3 - cell_2
    except ValueError as err:
        print(err)  # недопустимая операция

    try:
        cell_1 * 123
    except TypeError as err:
        print(err)  # действие допустимо только для экземпляров того же класса