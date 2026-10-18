from OOP_Homework4 import *

car = Car()

try:
    car.input_car()
    print("Tributes about cars:")
    car.show_car()
except ValueError as error:
    print("Error:", error)

print("Number of cars:", Car.get_counter())

print()

book = Book()

try:
    book.input_book()
    print("Data about the book:")
    book.show_book()
except ValueError as error:
    print("Error:", error)

print("Number of books:", Book.get_counter())

print()

stadium = Stadium()

try:
    stadium.input_stadium()
    print("Information about the stadium:")
    stadium.show_stadium()
except ValueError as error:
    print("Error:", error)

print("Number of stadiums:", Stadium.get_counter())
