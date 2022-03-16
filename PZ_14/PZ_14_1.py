# -*- coding: utf-8 -*-
import re
file = open('writer.txt', 'r', encoding = "utf-8")
all = file.readlines()
w_num = 0
output = []
for i in range(2, len(all) - 1):
    surname = re.search('[А-Я][а-я]*', all[i])[0]
    years = re.search('[0-9]{4}\s*-[0-9]{4}', all[i])[0]
    works = re.findall('«\D*?»', all[i])
    w_num += len(works)
    output.append([surname, years, works])
for i in range(len(output)):
    print(output[i][0])
for i in range(len(output)):
    print(output[i][1])
for i in range(len(output)):
    if len(output[i][2]) > 0:
        print(', '.join(output[i][2]))