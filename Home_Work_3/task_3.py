# 3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи
# влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все
# возможные варианты комплектации рюкзака.

from itertools import permutations, combinations

LOAD_CAPACITY = 10
list_items = {'палатка': 5, 'спальник': 3, 'горелка': 2, 'термос': 2, 'вода': 3}


def fill_bag(items_dict: dict[str:int]) -> dict[str:int]:
    bag = {}

    for key, value in items_dict.items():
        if sum(bag.values()) <= LOAD_CAPACITY:
            bag[key] = value
    bag.popitem()
    return bag


print(fill_bag(list_items))
