import time


def measure_time(function):
    def wrapper(n):
        start_time = time.time()

        result = function(n)

        end_time = time.time()

        print("Function execution time:", round(end_time - start_time, 3), "seconds")

        return result

    return wrapper


@measure_time
def calculate_sum(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total


result = calculate_sum(1_000_000)
print("Sum of numbers:", result)