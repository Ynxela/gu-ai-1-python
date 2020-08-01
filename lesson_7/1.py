"""Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31   22
37   43
51   86

3   5   32
2   4   6
-1  64  -8

3   5   8   3
8   3   7   1



Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix.
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    @staticmethod
    def _add_row_elements(first, second):
        return [first[i] + second[i] for i in range(len(first))]

    def __add__(self, other):
        return self.__class__(
            [
                [
                    self.matrix[row_idx][item_idx] + other.matrix[row_idx][item_idx]
                    for item_idx in range(len(self.matrix[row_idx]))
                ]
                for row_idx in range(len(self.matrix))
            ]
        )

    def __str__(self):
        mt = ''
        for row in self.matrix:
            for item in row:
                mt += f"{item:8d}"
            mt += '\n'
        return mt


mt_1 = Matrix(
    [
        [1, 2, 3],
        [10, 20, 30],
        [40, 50, 60],
        [100, 200, 300],
        [1000, 2000, 3000]
    ]
)

mt_2 = Matrix(
    [
        [4, 3, 2],
        [5, 5, 5],
        [10, 10, 10],
        [99, 98, 97],
        [-1, -1, -1]
    ]
)

mt_3 = mt_1 + mt_2
mt_4 = mt_2 + mt_3

print(mt_1)
print(mt_2)
print(mt_3)
print(mt_4)
