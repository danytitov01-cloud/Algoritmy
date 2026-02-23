import random

rows = int(input("Введите количество строк:"))
cols = int(input("Введите колчиство столбцов:"))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(1, 20))
    matrix.append(row)

for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()

total = 0
maximum = matrix[0][0]

for i in range(rows):
    for j in range(cols):
        total += matrix[i][j]
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]

print("Cумма всех элементов:",total)
print("Максимальный элеммент ",maximum)