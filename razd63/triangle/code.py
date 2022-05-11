import math

def triangle_perimetr():
    print("Команды: 1-Ввести свой радиус.  2-Использовать дефолтный радиус.")
    n = int(input("Выберите команду 1/2: "))
    while (n != 1) and (n != 2):
        try:
            print("Такой команды нет")
            n = int(input("Выберите команду 1/2: "))
        except ValueError:
            pass
    if n == 1:
        a = int(input("Введите сторну a: "))
        b = int(input("Введите сторну b: "))
        c = int(input("Введите сторну c: "))
    else:
        a = default_a
        b = default_b
        c = default_c
    p = a + b + c
    print("Периметр треугольника = ", p)


def triangle_area():
    print("Команды: 1-Ввести свой радиус.  2-Использовать дефолтный радиус.")
    n = int(input("Выберите команду 1/2: "))
    while (n != 1) and (n != 2):
        try:
            print("Такого команды нет")
            n = int(input("Выберите команду 1/2: "))
        except ValueError:
            pass
    if n == 1:
        a = int(input("Введите сторну a: "))
        b = int(input("Введите сторну b: "))
        c = int(input("Введите сторну c: "))
    else:
        a = default_a
        b = default_b
        c = default_c
    pp = (a + b + c) / 2
    s = math.sqrt(pp*(pp-a)*(pp-b)*(pp-c))
    print("Площадь теугольника = ", s)


default_a = 7
default_b = 2
default_c = 8