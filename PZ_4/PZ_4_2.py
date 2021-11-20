# Дано целое число N (> 0).
# С помощью операций деления нацело и взятия остатка от деления
# определить, имеются ли в записи числа N нечетные цифры.
# Если имеются, то вывести TRUE, если нет — вывести FALSE.
n = input('Введите число: ')
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print('Введено неверное число')
        n = input('Введите число: ')
    try:
        while n < 0:
            print('Введено неверное число')
            n = input('Введите число: ')
    except TypeError:
        continue
a = 0
while n > 0:
    if n % 2 != 0:
        a = 1
        n = n // 10
    else:
        a = 0
        n = n // 10
if a == 1:
    print('True')
else:
    print("False")
