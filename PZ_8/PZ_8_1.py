# Вариант 2
#
s = 'Петров Иван ПОКС-29 5 4 3 2 5 4 4 5 4'
student = {}
s = s.split()
student['Фамилия'] = s[0]
student['Имя'] = s[1]
student['Группа'] = s[2]
student['Оценки'] = []

for i in s[4:]:
    student['Оценки'].append(int(i))
a = sum(student['Оценки']) / len(student['Оценки'])

student['Среднее арифметическое оценок'] = a

print(student)