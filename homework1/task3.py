
countries = {"США", "Польща", "Південна Корея", "Франція"}

while True:
    print("\n1. Додати країну")
    print("2. Видалити країну")
    print("3. Пошук за символами")
    print("4. Перевірити наявність країни")
    print("5. Показати всі країни")
    print("0. Вийти")

    choice = input("Виберіть дію: ")

    if choice == "1":
        country = input("Введіть назву країни: ")
        countries.add(country)
        print("Країну додано")

    elif choice == "2":
        country = input("Введіть назву країни: ")

        if country in countries:
            countries.remove(country)
            print("Країну видалено")
        else:
            print("Країну не знайдено")

    elif choice == "3":
        symbols = input("Введіть символи для пошуку: ")

        for country in countries:
            if symbols.lower() in country.lower():
                print(country)

    elif choice == "4":
        country = input("Введіть назву країни: ")

        if country in countries:
            print("Країна є в множині")
        else:
            print("Країни немає в множині")

    elif choice == "5":
        print(countries)

    elif choice == "0":
        break

    else:
        print("Неправильний вибір")