# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json


def is_uniqe(data: dict, id_: str) -> bool:
    for item in data.values():
        if id_ in item.keys():
            return False
    return True


def enter_data(name_file: str) -> None:
    name_file += '.json'

    while True:
        id_ = input('Введите id:')
        name = input('Введите имя:')
        level = input('Введите уровень доступа:')

        try:
            with open(name_file, 'r', encoding='utf-8') as fr:
                read_dict: dict = json.load(fr)
        except FileNotFoundError:
            read_dict: dict = {str(i): {} for i in range(1, 8)}

        if is_uniqe(read_dict, id_):
            read_dict[level].update({id_: name})
        else:
            print('id не уникально')
        with open(name_file, 'w', encoding='utf-8') as fw:
            json.dump(read_dict, fw, indent=2)


__all__ = ['enter_data']

if __name__ == '__main__':
    enter_data('task_2')
