n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
summ = 0
for i in range(int(round(len(matrix) / 3, 0))):
    for j in range(len(matrix[i])):
        if matrix[i][j] < 0:
            summ += matrix[i][j]
print(summ)