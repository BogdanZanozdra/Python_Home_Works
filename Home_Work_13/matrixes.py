"""
Задача 1. Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

Задача 3. Создайте класс Матрица.
Добавьте методы для: - вывода на печать,
- сравнения,
- сложения,
- *умножения матриц
"""
from Home_Works.Home_Work_13 import exceptions
from exceptions import MultiplyMatrixException, AddMatrixException, TypeMatrixException
import numpy
""" Создайте класс Матрица.
Добавьте методы для: - вывода на печать,
- сравнения,
- сложения,
- *умножения матриц"""


class Matrix:
    def __init__(self, matrix):
        if exceptions.TypeMatrixException.get_type_element(matrix, matrix):
            raise TypeMatrixException(matrix)
        self.matrix = numpy.array(matrix)

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise AddMatrixException(len(self.matrix[0]), len(self.matrix),
                                     len(other.matrix[0]), len(other.matrix))
        return self.matrix + other.matrix

    def __mul__(self, other):
        if len(self.matrix) != len(other.matrix[0]) or len(self.matrix[0]) != len(other.matrix):
            raise MultiplyMatrixException(len(self.matrix[0]), len(self.matrix),
                                     len(other.matrix[0]), len(other.matrix))
        return self.matrix.dot(other.matrix)

    def __eq__(self, other):
        return numpy.array_equal(self.matrix, other.matrix)

    def __str__(self):
        return numpy.array_str(self.matrix)


if __name__ == '__main__':
    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    print(m1)
    m2 = Matrix([[1, 2, 3], [4, 5, 7]])
    print(m1+m2)
    m3 = Matrix([[1, 2], [4, 5], [3, 4]])
    print(m2*m3)
    print(m1 == m2)
