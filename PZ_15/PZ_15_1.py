# -*- coding: utf-8 -*-
n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
min = [0, 0]
max = [0, 0]
for i in range(n):
    for j in range(len(matrix[0])):
        if matrix[i][j] < matrix[min[0]][min[1]]:
            min = [i, j]
        elif matrix[i][j] > matrix[max[0]][max[1]]:
            max = [i, j]
print(matrix[min[0]][min[1]], matrix[max[0]][max[1]])