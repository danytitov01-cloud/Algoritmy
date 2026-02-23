import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 20))
    matrix.append(row)

print("\nМатрица:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()

row_sums = []

print("\nСуммы строк:")
for i in range(rows):
    s = 0
    for j in range(cols):
        s += matrix[i][j]
    row_sums.append(s)
    print("Строка", i, ":", s)

print("\nСуммы столбцов:")
for j in range(cols):
    s = 0
    for i in range(rows):
        s += matrix[i][j]
    print("Столбец", j, ":", s)

max_index = 0
for i in range(1, rows):
    if row_sums[i] > row_sums[max_index]:
        max_index = i

print("\nСтрока с максимальной суммой:", max_index)