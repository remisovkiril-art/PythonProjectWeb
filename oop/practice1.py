class Person:
    __counter = 0

    def __init__(self, pib="", birth_date="", phone="", city="", country="", address="", age=18):
        self.__pib = pib
        self.__birth_date = birth_date
        self.__phone = phone
        self.__city = city
        self.__country = country
        self.__address = address
        self.age = age
        Person.__counter += 1

    @property
    def pib(self):
        return self.__pib

    @pib.setter
    def pib(self, new_pib):
        if new_pib == "":
            raise ValueError("ПІБ не може бути порожнім")
        self.__pib = new_pib

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 0 or new_age >= 120:
            raise ValueError(f"Invalid Age {new_age}")
        self.__age = new_age

    @staticmethod
    def get_counter():
        return Person.__counter

    def input_person(self):
        self.pib = input("Введіть ПІБ: ")
        self.__birth_date = input("Введіть дату народження: ")
        self.__phone = input("Введіть контактний телефон: ")
        self.__city = input("Введіть місто: ")
        self.__country = input("Введіть країну: ")
        self.__address = input("Введіть домашню адресу: ")
        self.age = int(input("Введіть вік: "))

    def show_person(self):
        print("ПІБ:", self.pib)
        print("Дата народження:", self.__birth_date)
        print("Контактний телефон:", self.__phone)
        print("Місто:", self.__city)
        print("Країна:", self.__country)
        print("Домашня адреса:", self.__address)
        print("Вік:", self.age)