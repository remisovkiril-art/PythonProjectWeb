
cars = ["Koenigsegg Agera", "Bugatti", "Tesla", "BMW", "Ford", "Koenigsegg Agera", "Audi"]

name = input("Введите название производителя: ")
replacement = input("Введите слово для замены: ")

for i in range(len(cars)):
    if cars[i] == name:
        cars[i] = replacement

print("Список после замены:", cars)