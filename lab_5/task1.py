n = int(input("Введите количество элементов: "))

numbers = []
if n >0:
    for i in range(n):
        num = int(input("Введите число: "))
        numbers.append(num)
else:
    print("введите число больше нуля:")
print("Полученный массив:", numbers)