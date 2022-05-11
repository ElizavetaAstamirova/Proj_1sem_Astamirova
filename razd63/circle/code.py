# -*- coding: utf-8 -*-
def circle_perimetr(d_r=5):
    r = input("Введите радиус окружности: ")
    while type(r) != int:
        try:
            r = int(r)
        except ValueError:
            r = d_r
    pi = 3.14
    p = 2*pi*r
    print('Длина окружности = ', p)


def circle_area(d_r=5):
    r = input("Введите радиус окружности: ")
    while type(r) != int:
        try:
            r = int(r)
        except ValueError:
            r = d_r
    pi = 3.14
    s = pi*r**2
    print("Площадь окружности: ", round(s, 2))
