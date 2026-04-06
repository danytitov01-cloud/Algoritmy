phone_book = {
    "Danya": "87001111111",
    "Danial": "87002222222",
    "Maks": "87003333333",
    "Diyar": "87004444444",
    "Beka": "87005555555"
}

name = input("Введите имя: ")

if name in phone_book:
    print(phone_book[name])
else:
    print("Не найдено")