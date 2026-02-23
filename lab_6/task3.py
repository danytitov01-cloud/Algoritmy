import random

matrix = []

for i in range(4):
    row = []
    for j in range(4):
        row.append(random.randint(0, 9))
    matrix.append(row)

print("Поле 4x4 до передвежения:")

for i in range(4):
    for j in range(4):
        print(matrix[i][j], end=" ")
    print()

for i in range(4):
    new_row = []

    for j in range(4):
        if matrix[i][j] != 0:
            new_row.append(matrix[i][j])

    while len(new_row) < 4:
        new_row.insert(0, 0)

    matrix[i] = new_row

print("\nПоле 4x4 после передвежения вправо:")

for i in range(4):
    for j in range(4):
        print(matrix[i][j], end=" ")
    print()