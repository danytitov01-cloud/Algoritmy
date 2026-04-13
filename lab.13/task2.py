#Блок 2 - Логарифмическая сложность 
n = 1000
i = 1
steps = 0

while i < n:
    i *= 2
    steps += 1
    print("i =", i)

print("Количество шагов:", steps)