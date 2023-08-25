import csv
import json


def json_to_csv(name_file: str):
    with open(f'{name_file}.json', 'r') as f_inp:
        data = json.load(f_inp)
    rows = []
    for level, users in data.items():
        for id, name in users.items():
            rows.append({'level': level,
                        'name': name,
                         'id': id})
    with open(f'{name_file}.csv', 'w', newline='') as res:
        csv_write = csv.DictWriter(res, fieldnames=['level', 'name', 'id'])
        csv_write.writeheader()
        csv_write.writerows(rows)


if __name__ == '__main__':
    json_to_csv('users')
