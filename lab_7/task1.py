def add(a, b):
    return a + b


def power(a, n=2):
    return a ** n


def sum_all(*args):
    total = 0
    for x in args:
        total += x
    return total


print(add(2, 3))
print(power(4))
print(power(2, 3))
print(sum_all(1, 2, 3, 4))