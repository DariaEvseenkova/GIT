age = int(input("Введите ваш возраст:\n"))

if 7 <= age <= 18:
    print("Иди делай домашку")
elif 18 < age < 50:
    print("Доступ разрешен")
elif age >= 50:
    health = input("Как вы себя чувствуете?\n")

    if health == "хорошо" or "Хорошо":
        print("Поздравляю, доступ разрешен!")
else:
    print("Ошибка сервера")
