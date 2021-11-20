# Даны два целых числа A и B (A &lt; B).
# Вывести в порядке убывания все целые числа, расположенные между A и B (не включая числа A и B),
# а также количество N этих чисел.
a = input("Введите первое число: ")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")

b = input("Введите второе число: ")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")

k = 0
b -= 1
while a < b:
    print(b)
    b -= 1
    k += 1
print("Количество элементов =: ", k)