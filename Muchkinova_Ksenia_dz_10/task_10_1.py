from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for row in matrix:
            if len(row) != len(matrix[0]):
                raise ValueError('fail initialization matrix')


    def __str__(self):
        #return '\n'.join([f'| {" ".join(map(str, row))} |' for row in self.matrix])
        #return '\n'.join((map(str, self.matrix)))
        return  str('\n'.join(['\t'.join(str(el) for el in i) for i in self.matrix]))

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for el in range(len(other.matrix[i])):
                self.matrix[i][el] = self.matrix[i][el] + other.matrix[i][el]
        return Matrix.__str__(self)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    """
    | 1 2 |
    | 3 4 |
    | 5 6 |
    """
    print(first_matrix + second_matrix)
    """
    | 7 7 |
    | 7 7 |
    | 7 7 |
    """
    #fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])
    #print(fail_matrix)
    """
    Traceback (most recent call last):
      ...
    ValueError: fail initialization matrix
    """