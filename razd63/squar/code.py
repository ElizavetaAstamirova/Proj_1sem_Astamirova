def square_perimetr():
    print("Команды: 1-Ввести свои стороны.  2-Использовать дефолтные стороны.")
    n = int(input("Выберите команду 1/2: "))
    while (n != 1) and (n != 2):
        try:
            print("Такой команды нет")
            n = int(input("Выберите число 1/2: "))
        except ValueError:
            pass
    if n == 1:
        a = int(input("Введите сторjну a: "))
    else:
        a = default_a
    p = a*4
    print("Периметр квадрата = ", p)


def square_area():
    print("Команды: 1-Ввести свои стороны.  2-Использовать дефолтные стороны.")
    n = int(input("Выберите команду 1/2: "))
    while (n != 1) and (n != 2):
        try:
            print("Такой команды нет")
            n = int(input("Выберите команду 1/2: "))
        except ValueError:
            pass
    if n == 1:
        a = int(input("Введите сторjну a: "))
    else:
        a = default_a
    s = a**2
    print("Площадь квадрата = ", s)


default_a = 15