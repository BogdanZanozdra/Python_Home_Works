# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import json
from random import randint
import csv


def csv_gen(file_name: str):
    res = []
    with open(f'{file_name}.csv', 'w', newline='') as fw:
        csv_writer = csv.DictWriter(fw, fieldnames=['a', 'b', 'c'], quoting=csv.QUOTE_NONNUMERIC)
        for row in range(randint(MIN_ROWS, MAX_ROWS)):
            res.append({'a': randint(1, 9),
                        'b': randint(1, 9),
                        'c': randint(1, 9)})
        csv_writer.writeheader()
        csv_writer.writerows(res)


def cache_func(func: callable):
    try:
        with open(f'{func.__name__}.json', 'r', encoding='utf-8') as fr:
            data = json.load(fr)
    except FileNotFoundError:
        data = {}

    def wrapper(*args, **kwargs):
        arg_string = str(args) + str(kwargs)
        res_data = data.get(arg_string)
        if res_data:
            return res_data
        res = func(*args, **kwargs)
        data.update({arg_string: res})
        with open(f'{func.__name__}.json', 'w', encoding='utf-8') as fw:
            json.dump(data, fw, indent=4)
        return res
    return wrapper


def data_file(file_name):
    def push_numbers(func):
        def wrapper(*args, **kwargs):
            with open(f'{file_name}.csv', 'r', newline='') as fr:
                data = csv.reader(fr, quoting=csv.QUOTE_NONNUMERIC)

                for i, row in enumerate(data):
                    if i == 0:
                        continue
                    print(row)
                    result = func(*row)
                    print(result)
        return wrapper
    return push_numbers


csv_name = 'numbers'
MIN_ROWS = 10
MAX_ROWS = 20


@data_file(csv_name)
@cache_func
def quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d != 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        res = 'x1 =' + str(x1) + ' x2 = ' + str(x2)
    else:
        x = (-b) / (2 * a)
        res = 'x=' + str(x)
    return res

csv_gen(csv_name)
quadratic_equation(1, -6, 3)

