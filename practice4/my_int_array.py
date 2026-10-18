class MyIntArray:
    def __init__(self, values):
        for value in values:
            if not isinstance(value, int):
                raise TypeError("Array must contain only integers")
        self._values = values.copy()

    def __str__(self):
        result = ""
        for key in range(len(self._values)):
            result += f"{key}: {self._values[key]}\n"
        return result

    def __add__(self, other):
        if isinstance(other, MyIntArray):
            if len(self._values) == len(other._values):
                result = []
                for i in range(len(self._values)):
                    result.append(self._values[i] + other._values[i])
                return MyIntArray(result)
            return None

        if isinstance(other, int):
            result = []
            for value in self._values:
                result.append(value + other)
            return MyIntArray(result)

        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, MyIntArray):
            if len(self._values) == len(other._values):
                result = []
                for i in range(len(self._values)):
                    result.append(self._values[i] * other._values[i])
                return MyIntArray(result)
            return None

        if isinstance(other, int):
            result = []
            for value in self._values:
                result.append(value * other)
            return MyIntArray(result)

        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, MyIntArray):
            return self._values == other._values
        return False

    def __getitem__(self, index):
        if isinstance(index, int):
            if index >= 0 and index < len(self._values):
                return self._values[index]
        return "Invalid Index"

    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")

        if isinstance(index, int):
            if index >= 0 and index < len(self._values):
                self._values[index] = value
