age = int(input())
if age >= 50:
    health = input("Как вы себя чувствуете?")
    if health == "хорошо" or "Хорошо":
        print("Поздравляю, доступ разрешен!")
elif 7 <= age <= 18:
    print("Иди делай домашку")
elif age > 18:
    print("Доступ запрещен")
else:
    print("Ошибка сервера")
