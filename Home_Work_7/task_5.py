# Создайте функцию для сортировки файлов по директориям:
# видео, изображения, текст и т.п. Каждая группа включает
# файлы с несколькими расширениями. В исходной папке должны
# остаться только те файлы, которые не подошли для сортировки.

from os import chdir, listdir, mkdir, replace, path

__all__ = ['sort_files']


def sort_files(directory: str = 'test_dir'):
    chdir(directory)
    print(listdir())
    for file in listdir():
        if path.isdir(file):
            continue
        ext = file.split('.')[1]
        if ext.upper() not in listdir():
            mkdir(ext.upper())
        replace(file, f'{ext.upper()}\\{file}')


if __name__ == '__main__':
    sort_files()

