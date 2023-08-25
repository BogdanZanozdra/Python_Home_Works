# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import json
import pickle
import os


def json_to_pickle(dir: str = 'Sem_8'):
    files = list(filter(lambda x: '.json' in x, os.listdir()))
    for file in files:
        filename, *_ = file.split('.')
        with (open(file, 'r') as source, open(f'{filename}.pickle', 'wb') as res):
            data = json.load(source)
            pickle.dump(data, res)


if __name__ == '__main__':
    json_to_pickle()
