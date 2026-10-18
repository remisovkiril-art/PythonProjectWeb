class Car:
    __counter = 0

    def __init__(self, model="", year=2020, manufacturer="", engine_volume=1.0, color="", price=0):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color = color
        self.price = price
        Car.__counter += 1

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        if new_model == "":
            raise ValueError("Model name cannot be empty")
        self.__model = new_model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        if new_year < 1886 or new_year > 2026:
            raise ValueError("Incorrect year of manufacture")
        self.__year = new_year

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = new_price

    @staticmethod
    def get_counter():
        return Car.__counter

    def input_car(self):
        self.model = input("Enter the car model: ")
        self.year = int(input("Enter the year of release: "))
        self.__manufacturer = input("Enter the manufacturer: ")
        self.__engine_volume = float(input("Enter engine displacement: "))
        self.__color = input("Enter the color of the car: ")
        self.price = float(input("Enter the price of the car: "))

        if self.__engine_volume <= 0:
            raise ValueError("Engine displacement must be greater than zero")

    def show_car(self):
        print("Model:", self.model)
        print("Year of release:", self.year)
        print("Producer:", self.__manufacturer)
        print("Engine volume:", self.__engine_volume)
        print("Color:", self.__color)
        print("Price:", self.price)


class Book:
    __counter = 0

    def __init__(self, title="", year=2020, publisher="", genre="", author="", price=0):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.price = price
        Book.__counter += 1

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, new_title):
        if new_title == "":
            raise ValueError("Book title cannot be empty")
        self.__title = new_title

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        if new_year < 0 or new_year > 2026:
            raise ValueError("Wrong year of publication")
        self.__year = new_year

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = new_price

    @staticmethod
    def get_counter():
        return Book.__counter

    def input_book(self):
        self.title = input("Enter book title: ")
        self.year = int(input("Enter publication year: "))
        self.__publisher = input("Enter publisher: ")
        self.__genre = input("Enter genre: ")
        self.__author = input("Enter author: ")
        self.price = float(input("Enter book price: "))

    def show_book(self):
        print("Book title:", self.title)
        print("Publication year:", self.year)
        print("Publisher:", self.__publisher)
        print("Genre:", self.__genre)
        print("Author:", self.__author)
        print("Price:", self.price)


class Stadium:
    __counter = 0

    def __init__(self, name="", opening_date="", country="", city="", capacity=0):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.capacity = capacity
        Stadium.__counter += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            raise ValueError("The stadium name cannot be empty")
        self.__name = new_name

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, new_capacity):
        if new_capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self.__capacity = new_capacity

    @staticmethod
    def get_counter():
        return Stadium.__counter

    def input_stadium(self):
        self.name = input("Enter stadium name: ")
        self.__opening_date = input("Enter opening date: ")
        self.__country = input("Enter country: ")
        self.__city = input("Enter city: ")
        self.capacity = int(input("Enter stadium capacity: "))

    def show_stadium(self):
        print("Stadium name:", self.name)
        print("Opening date:", self.__opening_date)
        print("Country:", self.__country)
        print("City:", self.__city)
        print("Capacity:", self.capacity)