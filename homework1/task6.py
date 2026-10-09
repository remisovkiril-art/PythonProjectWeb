
capitals = {
    "Україна": "Київ",
    "Польща": "Варшава",
    "Німеччина": "Берлін",
    "Франція": "Париж"
}

while True:
    print("\n1. Додати країну")
    print("2. Видалити країну")
    print("3. Знайти столицю")
    print("4. Замінити столицю")
    print("5. Показати всі країни та столиці")
    print("0. Вийти")

    choice = input("Виберіть дію: ")

    if choice == "1":
        country = input("Введіть назву країни: ")
        capital = input("Введіть столицю: ")

        capitals[country] = capital
        print("Дані додано")

    elif choice == "2":
        country = input("Введіть назву країни: ")

        if country in capitals:
            del capitals[country]
            print("Країну видалено")
        else:
            print("Країну не знайдено")

    elif choice == "3":
        country = input("Введіть назву країни: ")

        if country in capitals:
            print("Столиця:", capitals[country])
        else:
            print("Країну не знайдено")

    elif choice == "4":
        country = input("Введіть назву країни: ")

        if country in capitals:
            capital = input("Введіть нову столицю: ")
            capitals[country] = capital
            print("Столицю замінено")
        else:
            print("Країну не знайдено")

    elif choice == "5":
        print(capitals)

    elif choice == "0":
        break

    else:
        print("Неправильний вибір")