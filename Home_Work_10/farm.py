# Задача 1. Доработаем задания 5-6. Создайте класс-фабрику.
# - Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# - Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

from animals import Dog, Birds, Animal


class Factory:
    animal_types = {
        'dog': Dog,
        'bird': Birds}

    def create_animal(self, animal_type, *args, **kwargs):
        return self.animal_types.get(animal_type, Animal)(*args, **kwargs)


if __name__ == '__main__':
    animal1 = Factory()
    print(animal1.create_animal('bird', 'Dacker', 7,'white', 'cock', True, False, 'jjj'))
