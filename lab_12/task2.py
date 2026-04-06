numbers = [5, 2, 5, 3, 2, 5]

count = {}

for num in numbers:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

print(count)
