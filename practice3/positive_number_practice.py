class PositiveNumber:
    def __new__(cls, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")

        if value < 0:
            print("Negative numbers are not allowed")
            return None

        return super().__new__(cls)

    def __init__(self, value):
        self.value = value


a = PositiveNumber(10)
b = PositiveNumber(-5)

print(a.value)
print(b)
