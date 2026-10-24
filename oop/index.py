def values_in_range(numbers, start, end):
    for number in numbers:
        if start <= end:
            if start <= number <= end:
                yield number
        else:
            if end <= number <= start:
                yield number


numbers = [1, 5, 10, 15, 20, 25, 30]

start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))

generator = values_in_range(numbers, start, end)

for number in generator:
    print(number)