# Задача 1. Доработаем задания 5-6. Создайте класс-фабрику.
# - Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# - Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
#
# Задача 3. Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задания должны решаться через вызов методов (экземпляра.
# Задача)


class Animal:
    def __init__(self, name, age, *args, **kwargs):
        self.name = name.capitalize()
        self.age = age

    def __str__(self):
        return f'{self.name}, {self.age}'

    def birthday(self):
        self.age += 1


class Dog(Animal):
    def __init__(self,
                 name: str,
                 age: int,
                 color: str,
                 breed: str,
                 is_domestic: bool,
                 *args, **kwargs):
        super().__init__(name, age)
        self.color = color
        self.breed = breed
        self.is_domestic = is_domestic

    def __str__(self):
        if self.is_domestic:
            return f'Dog {self.name} {self.breed} домашняя'
        return f'Dog {self.name} {self.breed} уличная'


class Birds(Animal):
    def __init__(self,
                 name: str,
                 age: int,
                 color: str,
                 breed: str,
                 is_domestic: bool,
                 is_flying: bool,
                 *args, **kwargs):
        super().__init__(name, age)
        self.color = color
        self.breed = breed
        self.is_domestic = is_domestic
        self.is_flying = is_flying

    def __str__(self):
        return f'Bird {self.breed}, {self.color}, {self.age}, is_domestic: {self.is_domestic}'


class Factory:
    def __init__(self, animal_type, name, age, *args, **kwargs):
        self.animal_type = animal_type
        self.name = name
        self.age = age
        if self.animal_type == Dog:
            self.color = args[0]
            self.breed = args[1]
            self.is_domestic = args[2]
        elif self.animal_type == Birds:
            self.color = args[0]
            self.breed = args[1]
            self.is_domestic = args[2]
            self.is_flying = args[3]

    factory_animal = (Dog, 'Grem', 4, 'black', 'Labrador', True)

    def __str__(self):
        return f'{self.animal_type}, {self.name}, {self.age}, {self.color}, {self.breed}'


if __name__ == '__main__':

    factory_animal = Factory(Dog, 'Grem', 4, 'black', 'Labrador', True)
    print(factory_animal)
    factory_animal_2 = Factory(Birds,'Dacker', 7,'white', 'cock', True, False)
    print(factory_animal_2)
    # animal = Animal('name', 3)
    # print(animal)
    # dog = Dog('Setter', 2, 'red', 'Labr', False)
    # print(dog)
    # bird = Birds('Dacker', 7,'white', 'cock', True, False )
    # print(bird)
    # bird.birthday()
    # print(bird)