from practice1 import Person


class User:
    __counter = 10
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __init__(self, name='unknown', age=18):
        self.__name = name
        self.__age = age
        self._email = 'admin@gmai.com'
        self._phone = '+380 00 000 00 00'

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if 0 < new_age <= 120:
            self.__age = new_age

    def __str__(self):
        return f'User: {self.__name}, Age: {self.__age}'

    def show_user(self):
        return f'User: {self.__name}, Age: {self.__age}'
    @staticmethod
    def get_counter():
        return User.__counter
    def __del__(self):
        print('__del__')
    def __add__(self, other):
        if isinstance(other, User):
            self.__name += '' + other.__name
        if isinstance(other, int):
            self.__age += other
    def __mul__(self, other):
        self.__age *= other