def horizontal_line(symbol):
    print(symbol * 10)


def vertical_line(symbol):
    for i in range(10):
        print(symbol)


def show_line(symbol, function_to_call):
    function_to_call(symbol)


symbol = input("Enter a symbol: ")
line = input("Choose a line (horizontal or vertical): ")

if line == "horizontal":
    show_line(symbol, horizontal_line)
elif line == "vertical":
    show_line(symbol, vertical_line)
else:
    print("Invalid line type")