# Создайте функцию, которая создаёт файлы с указанным
# расширением. Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

# Доработаем предыдущую задачу. Создайте новую функцию которая генерирует файлы
# с разными расширениями. Расширения и количество файлов функция принимает в
# качестве параметров. Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно. Внутри используйте
# вызов функции из прошлой задачи.

from random import randint, choice
from os import getcwd, listdir, mkdir

__all__ = ['create_files']


def create_ext():
    ext = choice(EXTENSIONS)
    create_files(ext=ext)


def give_name() -> str:
    name: str = ''
    for _ in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()


def create_files(ext: str, directory: str = None,
                 min_len: int = 6, max_len: int = 30,
                 min_size: int = 256, max_size: int = 4096,
                 count_files: int = 2):
    if not directory:
        directory = getcwd() + '\\'
    else:
        if directory not in listdir():
            mkdir(directory)
        directory = getcwd() + '\\' + directory + '\\'
    for _ in range(count_files):
        with open(directory + give_name() + ext, 'w', encoding='utf-8') as file_output:
            list_of_bytes = bytes([randint(0, 255) for _ in range(min_size, max_size)])
            file_output.write(str(list_of_bytes))


if __name__ == '__main__':
    EXTENSIONS = ('.txt', '.pdf', '.doc')
    create_files(ext=choice(EXTENSIONS), directory='test_dir')
