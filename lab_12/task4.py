phone_book = {
    "Danya": "87471111111",
    "Danial": "87002222222",
    "Maks": "87083333333",
    "Diyar": "87474444444",
    "Beka": "87005555555"
}

name = input("Введите имя: ")

if name in phone_book:
    print(phone_book[name])
else:
    print("Не найдено")