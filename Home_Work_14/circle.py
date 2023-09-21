# Пишем тесты для задачи:

# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.
import math


class Circle:
    pi_ = math.pi

    def __init__(self, radius) -> None:
        if not isinstance(radius, (int, float)):
            raise TypeError('Radius must be an integer or float type!')
        elif radius <= 0:
            raise ValueError('Radius must be greater than 0!')
        else:
            self.radius = radius

    def calc_len(self):
        return self.pi_ * self.radius * 2

    def calc_area(self):
        return self.pi_ * self.radius ** 2


c1 = Circle(5)
print(c1.calc_len())
# print(c1.radius)

