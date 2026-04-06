products = {
    "apple": 100,
    "banana": 150
}

# добавление
products["orange"] = 200

# изменение
products["apple"] = 120

# удаление
del products["banana"]

# поиск
name = "apple"
print(products.get(name))