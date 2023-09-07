# Задание. Создайте класс студента.
# - Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# - Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# - Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# - Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
from random import randint
import csv, json


class FullName:
    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value):
        names = value.split(' ')
        for name in names:
            if not name.isalpha() or not name.istitle():
                raise ValueError('ФИО должны начинаться с заглавной буквы и должны содержать только буквы!')


class Student:
    full_name = FullName()

    def __init__(self, full_name):
        self.full_name = full_name
        with open('subjects.csv', 'r', encoding='utf-8') as f:
            subjects = f.readline().split(',')
        self.__subjects = {subjects[0]: None, subjects[1]: None, subjects[2]: None}

    def set_marks(self):
        self.__subjects["математика"] = {'оценка': randint(2, 5), 'тестирование': randint(1, 100)}
        self.__subjects["история"] = {'оценка': randint(2, 5), 'тестирование': randint(1, 100)}
        self.__subjects["физика"] = {'оценка': randint(2, 5), 'тестирование': randint(1, 100)}

    def average_mark(self):
        mark = 0
        for key, value in self.__subjects.items():
            mark += value['оценка'] / len(self.__subjects)
        return mark

    def get_subjects(self):
        return self.__subjects

    def __str__(self):
        return (f'Студент {self.full_name}, успеваемость: {self.__subjects}, '
                f'средняя оценка по всем предметам: {self.average_mark()}')


if __name__ == '__main__':
    s1 = Student('Закики Нарии Бро')
    print(s1.get_subjects())
    s1.set_marks()
    print(s1.get_subjects())
    print(s1.average_mark())
    print(s1)

    print(s1.get_subjects())
