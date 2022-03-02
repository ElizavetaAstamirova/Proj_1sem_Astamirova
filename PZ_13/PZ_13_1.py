# -*- coding: utf-8 -*-
# Организовать и вывести последовательность A из n чисел (n - четное).
# Из последовательности A получить две последовательности B и C:
# в последовательности B - первая половина элементов A, в C - вторая половина элементов A.
# Найти протизведение соответствующих элементов последовательностей B и C.
# Найти среднее арифметической полученной последователньости.
n, a, d = (int(input()), [], [])
for i in range(n):
    a.append(int(input()))
b, c = (a[:n // 2], a[n // 2:])
for i in range(n // 2):
    d.append(b[i] * c[i])
print(sum(d) / len(d))