# ЗАДАЧА 2: Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# # - К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
#
# Пример:
# rename(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
# foto_2002.txt -> o_20video001.csv
#
# ЗАДАЧА 3:Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

from os import listdir, rename, getcwd, path, chdir


def renaming_func(desired_name: str = 'video',
                  count_digits: int = 1,
                  source_file_ext: str = '.pdf',
                  final_file_ext: str = '.mp4',
                  letters_range: tuple = (1, 5),
                  working_directory: str = 'test_dir'):
    directory = working_directory
    chdir(directory)
    path_ = path.join(getcwd(), directory)
    for num, file in enumerate(listdir()):
        if path.isdir(file):
            continue
        current_ext = file.split('.')[1]
        if len(str(num)) == count_digits and current_ext == source_file_ext[1:]:
            create_name(file, desired_name, num, final_file_ext, letters_range)


def create_name(file: str = 'output.pdf', desired_name: str = 'video', num: int = 1,
                final_file_ext: str = '.doc',
                letters_range: tuple = (1, 6)):
    rename(file, f'{file[letters_range[0]: letters_range[1]]}{desired_name}{num}{final_file_ext}')


__all__ = ['renaming_func']

if __name__ == '__main__':
    renaming_func()
