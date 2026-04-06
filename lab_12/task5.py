words = ["cat", "dog", "cat", "bird", "dog", "dog"]

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for word in count:
    if count[word] > 1:
        print(word)