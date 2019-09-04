#__author__ = 'Гродзинский Дмитрий Александрович'# Задача-1:
from math import sqrt
# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def height(self):
        p = 1 / 2 * (self.a + self.b + self.c)
        h = sqrt((self.a ** 2) - (self.b ** 2 / 4))
        return round(h, 1)

    def square(self):
        h = Triangle.height(self)
        s = 1 / 2 * self.a * h
        return s

    def perimeter(self):
        p = self.a + self.b + self.c
        return p

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def equilateral(self):
        if self.a + self.b == self.c + self.d:
            return True
        else:
            return False

    def side_lengths(self):
        s = Trapeze.square(self)
        h = Trapeze.square(self)
        length = (2 * s) / h - self.b
        return length

    def perimeter(self):
        A = self.a + self.b
        B = self.b + self.c
        C = self.a + self.d
        p = 2 * A + B + C
        return p

    def square(self):
        h = sqrt((self.c ** 2) - (self.a - self.b) ** 2 / 4)
        s = 0.5 * (self.a + self.b) * h
        return round(s, 1)



