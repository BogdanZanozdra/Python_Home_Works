# 1. Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

matrix = [[1, 2, 3], [4, 5, 6]]


def transposition(input_matrix: list[list[int]]):
    res_matrix = []
    for i in range(len(input_matrix)):
        res_matrix = list(map(list, zip(*input_matrix)))
    return res_matrix


print(matrix)
print(transposition(matrix))
