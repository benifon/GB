# 1.

class Matrix:
    def __init__(self, matrix_data):
        self.matrix_data = matrix_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.matrix_data])

    def __add__(self, other):
        new_matrix = [
            [self.matrix_data[i][j] + other.matrix_data[i][j] for j in range(len(self.matrix_data[0]))]
            for i in range(len(self.matrix_data))]

        return Matrix(new_matrix)

matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])
print(matrix_1)
print(matrix_1 + matrix_2)

# 2.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, option):
        self.option = option

    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes):

    @property
    def calculate(self):
        return round((self.option / 6.5) + 0.5)


class Suit(Clothes):

    @property
    def calculate(self):
        return round((2 * self.option) + 0.3)


coat = Coat(130)
suit = Suit(265)
print(coat.calculate)
print(suit.calculate)

# 3.
class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'Ячеек в первой клетке меньше,чем во второй. Вычитание невозможно!'

    def __mul__(self, other):
        return 'Multiply of cells is ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Truediv of cells is ' + str(round(self.nums / other.nums))


cell_1 = Cell(13)
cell_2 = Cell(50)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2.make_order(10))

