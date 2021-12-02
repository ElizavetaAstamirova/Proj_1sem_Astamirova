# Вариант 2
# Описать функцию Mean(параметры), вычисляющую среднее арифметическое AMean
# (X+Y)/2 и среднее геометрическое GMean = y/X Y двух положительных
# чисел Х и Y. C помощью этой функции найти среднее арифметическое и среднее
# геометрическое для пар (A, B), (А, C), (A, D), если даны А, В, C, D.

def AMean(X, Y):
    return (X + Y) / 2


def GMean(X, Y):
    return Y / X


print('A: ')
A = float(input())
print('B: ')
B = float(input())
print('C: ')
C = float(input())
print('D: ')
D = float(input())
print(AMean(A, B), ' ', GMean(A, B))
print(AMean(A, C), ' ', GMean(A, C))
print(AMean(A, D), ' ', GMean(A, D))
