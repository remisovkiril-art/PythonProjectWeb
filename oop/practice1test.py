from practice1 import *

person = Person()

try:
    person.input_person()
    print("\nДані про людину:")
    person.show_person()
except ValueError as error:
    print("Помилка:", error)

print("Кількість об'єктів:", Person.get_counter())