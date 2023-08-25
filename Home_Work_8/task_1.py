# 1. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты
# обхода сохраните в файлы json, csv и pickle.
# 2. Для дочерних объектов указывайте родительскую директорию.
# 3. Для каждого объекта укажите файл это или директория.
# 4. Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
#
# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
# "name": names.txt
# "parent": users,
# "type": "file"
# "size": 4096
# }
#
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
import csv
import json
import os
import pickle


def get_size_file_in_direct(path: str) -> int:
  size = 0
  for dir_path, dir_names, file_names in os.walk(path):
    for file in file_names:
        fp = os.path.join(dir_path, file)
        size += os.path.getsize(fp)
  return size


def get_info(dir: str) -> list[dict]:
    os.chdir('..')
    os.chdir(dir)
    print(os.getcwd())
    res = []
    for dir_path, dir_name, file_name in os.walk(os.getcwd()):
        for dir in dir_name:
            *_, parent = dir_path.split('\\')
            res.append({'name': dir,
                        'parent': parent,
                        'type': 'directory',
                        'size': get_size_file_in_direct(dir_path + '\\' + dir)})
        for file in file_name:
            *_, parent = dir_path.split('\\')
            res.append({'name': file,
                        'parent': parent,
                        'type': 'file',
                        'size': os.path.getsize(os.path.join(os.getcwd(), dir_path, file))})
    return res


def write_json(file_name: str) -> None:
    with open(f'{file_name}.json', 'w') as f:
        res = get_info('Home_Work_7')
        json.dump(res, f, indent=2)


def write_csv(file_name: str) -> None:
    with open(f'{file_name}.csv', 'w', newline='') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=['name', 'parent', 'type', 'size'])
        res = get_info('Home_Work_7')
        csv_write.writeheader()
        csv_write.writerows(res)


def write_pickle(file_name: str) -> None:
    with open(f'{file_name}.pickle', 'wb') as p_file:
        pickle.dump(get_info('Home_Work_7'), p_file)


file_name = 'walk_task'

__all__ = ['get_info', 'write_csv', 'write_json', 'write_pickle']

if __name__ == '__main__':
    # info = get_info('Home_Work_7')
    # print(info)
    # write_json(file_name)
    # write_csv(file_name)
    write_pickle(file_name)
