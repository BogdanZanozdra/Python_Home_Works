# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.
import json


def csv_to_json(file_name: str):
    with open(f'{file_name}.csv', 'r', newline='') as f_csv:
        data = f_csv.read().split('\n')

    res: list = []
    data.pop()
    for value in data[1:]:
        level, name, id = value[:-1].split(',')
        res.append({'id': f'{int(id):06}',
                    'name': name,
                    'level': level,
                    'hash': hash(id+name)})

    with open(f'new_{file_name}.json', 'w', newline='') as f_json:
        json.dump(res, f_json, indent=4)


if __name__ == '__main__':
    csv_to_json('users')
    print(f'{6:10}')
