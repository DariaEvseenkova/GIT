age = int(input())
if age >= 50:
    health = input("Как вы себя чувствуете?")
    print(health)
    if health == "хорошо":
        print("Поздравляю!")
elif 7 < age < 18:
    print("Иди делай домашку")
elif age > 18:
    print("Доступ запрещен")
else:
    print("Доступ разрешен")
