import csv
import re
import logging
from collections import defaultdict
import argparse


def categorizing(file_name: str):
    FORMAT = 'Следующее письмо не отнесено ни к одной из категорий: "{msg}"'

    logging.basicConfig(filename='log.log',
                        encoding='utf-8',
                        format=FORMAT,
                        style='{',
                        level=logging.INFO)

    logger = logging.getLogger(__name__)

    result = defaultdict(list)

    KEYWORDS = {'Security': ['парол', 'безопас', 'заблок', 'разблок'],
                'Refunds': ['возвр', 'вернуть'],
                'Troubleshooting': ['неправил', 'отмен', 'проблем', 'ошиб', 'некоррект', 'исправ', 'баг'],
                'Account': ['аккаунт', 'парол', 'регистрац', 'авториз', 'пользовател', 'заблок', 'разблок', 'форм',
                            'учетн'],
                'Advertising and Collaboration': ['реклам', 'сотруднич', 'партнёр'],
                'Limits': ['лимит', 'ограниче'],
                'Payments': ['оплат'],
                'Features': ['функц', 'сервис', 'подписк', 'api']}

    cont = []

    with open('user_support_letters.csv', 'r', encoding='utf-8', newline='') as csv_file:

        csv_reader = csv.reader(csv_file)
        for line_ in csv_reader:
            for category, keyword_list in KEYWORDS.items():
                for keyword in range(len(keyword_list)):
                    if re.search(keyword_list[keyword], line_[0].lower()):
                        result[category].append(line_)
                        cont.append(line_[0])
            if line_[0] not in cont:
                logger.info(line_[0])

        with open('categorized_letters.csv', 'w', encoding='utf-8', newline='') as csv_writer:
            csv_write = csv.writer(csv_writer)
            for key, value in result.items():
                csv_write.writerow(key)
                print(f'{key}:')
                csv_write.writerows(value)
                print(value)


file_name = 'user_support_letters.csv'


def parse():
    parser = argparse.ArgumentParser(description='Categorization parser')
    parser.add_argument('-f', '--file_name', type=str)
    args = parser.parse_args()
    return categorizing(f'{args.file_name}')


if __name__ == '__main__':
    # categorizing('user_support_letters.csv')
    print(parse())
