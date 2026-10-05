def even_numbers(start, end):
    result = []

    for number in range(start, end + 1):
        if number % 2 == 0:
            result.append(number)

    return result


print(even_numbers(1, 10))