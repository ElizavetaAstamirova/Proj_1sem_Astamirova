# -*- coding: utf-8 -*-
# Составить список, в который будут включены только согласные буквы
# и привести их к верхнему регистру.
# Список: [«Оттава», «Москва», «Пекин», «Полоцк», «Версаль», «Дели», «Каир»].
cities = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели', 'Каир']
output = []
notthis = 'аяоёуюэеыи'
for i in range(len(cities)):
    cities[i] = cities[i].lower()
    for j in range(len(cities[i])):
        if not cities[i][j] in notthis:
            output.append(cities[i][j].upper())
print(output)
