# Задача 1 — Дубликаты
arr = [1, 2, 3, 2, 4, 1, 5]
duplicates = []
seen = set()

for num in arr:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    seen.add(num)

print("1) Дубликаты:", duplicates)


# Задача 2
arr = [1, 2, 2, 3, 3, 3, 4]
count = {}

for num in arr:
    count[num] = count.get(num, 0) + 1

max_num = max(count, key=count.get)
print("2) Самое частое число:", max_num)


# Задача 3 — Пара с заданной суммой
arr = [2, 7, 11, 15]
target = 9
seen = {}

for num in arr:
    complement = target - num
    if complement in seen:
        print(f"3) {complement} + {num} = {target}")
        break
    seen[num] = True


# Задача 4 — Сортировка строк по длине
strings = ["яблоко", "киви", "банан", "груша"]
strings.sort(key=len)
print("4) Сортировка:", strings)


# Задача 5 — Топ-3 слова
text = "привет мир привет мир привет python"
words = text.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

sorted_words = sorted(count.items(), key=lambda x: x[1], reverse=True)
print("5) Топ-3:", sorted_words[:3])


# Задача 6 — Удалить дубликаты
arr = [1, 2, 2, 3, 1, 4]
result = []
seen = set()

for num in arr:
    if num not in seen:
        result.append(num)
        seen.add(num)

print("6) Без дубликатов:", result)


# Задача 7 — Пересечение списков
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
result = list(set(a) & set(b))
print("7) Пересечение:", result)


# Задача 8 — Максимальный балл
students = {
    "Аня": 85,
    "Иван": 92,
    "Олег": 78
}

max_student = max(students, key=students.get)
print("8) Лучший студент:", max_student)


# Задача 9 — Чётные и нечётные
arr = [1, 2, 3, 4, 5, 6]
even = []
odd = []

for num in arr:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("9) Чётные:", even)
print("9) Нечётные:", odd)


# Задача 10 — Самая длинная последовательность
arr = [1, 1, 2, 2, 2, 3, 3]

max_len = 1
current_len = 1

for i in range(1, len(arr)):
    if arr[i] == arr[i - 1]:
        current_len += 1
        if current_len > max_len:
            max_len = current_len
    else:
        current_len = 1

print("10) Максимальная длина:", max_len)


# Задача 11 — Мини-система пользователей
users = {}

# добавление
users["Даня"] = 18
users["Аня"] = 20

# поиск
name = "Даня"
if name in users:
    print("11)", name, "возраст:", users[name])
else:
    print("11) Пользователь не найден")

# удаление
del users["Аня"]

print("11) Список пользователей:", users)