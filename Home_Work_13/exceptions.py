import numpy

import matrixes


class MatrixExceptions(Exception):
    pass


class AddMatrixException(MatrixExceptions):
    def __init__(self, a_length, a_height, b_length, b_height):
        self.a_length = a_length
        self.a_height = a_height
        self.b_length = b_length
        self.b_height = b_height

    def __str__(self):
        return (
            f"Размеры матриц должны быть одинаковыми. Ваша матрица а имеет {self.a_height} строк и {self.a_length} столбцов,"
            f" а матрица b - {self.b_height} строк и {self.b_length} столбцов!")


class TypeMatrixException(MatrixExceptions):
    def __init__(self, value):
        self.value = value
        self.wrong_elements = self.get_type_element(value)

    def get_type_element(self, matrix):
        wrong_type_elements = []
        for row in matrix:
            for element in row:
                if type(element) not in (int, float):
                    wrong_type_elements.append(element)
        return wrong_type_elements

    def __str__(self):
        self.value = numpy.array(self.value)
        return (f'Типом значений матрицы может быть целое int() или вещественное float() число \n'
                f'Ваша матрица:\n {self.value}\n'
                f'у Вас значения {self.wrong_elements} не валидного типа.')


class MultiplyMatrixException(MatrixExceptions):
    def __init__(self, a_length, a_height, b_length, b_height):
        self.a_length = a_length
        self.a_height = a_height
        self.b_length = b_length
        self.b_height = b_height

    def __str__(self):
        return ('Длинна и выста матрицы а должны быть равны высоте и длинне матрицы b соответственно.\n'
                f'Ваша матрица а имеет {self.a_height} строк и {self.a_length} столбцов,\n'
                f'а матрица b - {self.b_height} строк и {self.b_length} столбцов!')
