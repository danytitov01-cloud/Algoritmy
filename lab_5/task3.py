n = int(input("Введите количество элементов: "))

numbers = []

for i in range(n):
    num = int(input("Введите число: "))
    numbers.append(num)

positive = 0
negative = 0
even = 0

for num in numbers:
    if num > 0:
        positive += 1
    if num < 0:
        negative += 1
    if num % 2 == 0:
        even += 1

print("Массив:", numbers)
print("Количество положительных чисел:", positive)
print("Количество отрицательных чисел:", negative)
print("Количество чётных элементов:", even)