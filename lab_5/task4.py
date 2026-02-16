n = int(input("Введите количество элементов: "))

numbers = []

for i in range(n):
    num = int(input("Введите число: "))
    numbers.append(num)

target = int(input("Введите число для поиска: "))

found = False
index = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        found = True
        index = i
        break5
        

if found:
    print("Число найдено. Индекс:", index)
else:
    print("Число не найдено в массиве.")