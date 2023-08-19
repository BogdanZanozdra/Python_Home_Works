# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение
# — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
# Пример:rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}


def task2(**kwargs):
    types_list = [list, dict, bytearray, frozenset]
    res = {}
    for key, value in kwargs.items():
        if type(value) in types_list:
            res.setdefault(str(value), key)
        else:
            res.setdefault(value, key)

    return res

# types_list = [ list, dict, bytearray, frozenset]
# if type(types_list) in types_list:
#     print('ok')

print(task2(res=1, reverse=[1, 2, 3]))




