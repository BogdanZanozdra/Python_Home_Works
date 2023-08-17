# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами
# чисел. Первое число int, второе - float
# разделены вертикальной чертой. Минимальное
# число - -1000, максимальное - +1000. Количество строк и имя
# файла передаются как аргументы функции.

from random import randint, uniform

__all__ = ['fill_file']


def fill_file(name_file: str, count_line: int) -> None:
    with open(name_file, 'a', encoding='utf-8') as f:
        for _ in range(count_line):
            f.write(f'{randint(-100, 100)} | {uniform(-100, 100)} \n')


if __name__ == '__main__':
    fill_file('task_1.txt', 5)
