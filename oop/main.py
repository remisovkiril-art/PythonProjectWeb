# from abc import ABC, abstractmethod
#
# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#
# class Car(Transport):
#     def move(self):
#         print("Car moved")
#
# class Bus(Transport):
#     def move(self):
#         print("Bus moved")
#
#
# def drive(tr):
#     if isinstance(tr,Transport):
#         tr.move()
#
#
# def main():
#     drive(Car())
#     drive(Bus())
#     drive(type("Tank",(Transport,),{
#         'move':lambda self:print("Tank moved")
#     })())
#     # s = StudentOnline.from_string("Ivan:20")
#     # print(type(s))
#     # set1 = {1,2,4}  # create set
#     # set2 = {2,4,3,5,11,13}
#     # un = set1.difference(set2)
#     # print(un) # 2,3,4
#     # ^ XOR true ^ false =>true
#     # set1.add(2)
#     # print(set1)
#     # d2 = dict(name="Tom", surname="Due")
#     # d2["name"] = "Bob"
#     # for item in d2.items():
#     #     print(item)
#     # cities_1 = {"Київ", "Львів", "Одеса", "Харків"}
#     # cities_2 = {"Львів", "Одеса", "Дніпро", "Полтава"}
#     # cities_3 = cities_1 - cities_2
#     #
#     # print("\nПерша множина міст:", cities_1,sorted(cities_1))
#     #
#     # cities1 = {"Київ", "Львів", "Одеса"}
#     # cities2 = {"Львів", "Харків", "Одеса"}
#     # common_cities = cities1 & cities2
#     # print("\nСпільні міста:", common_cities)
#
#     # Higher Order Function
#     # get_sum = lambda x,y:x+y
#     # print(get_sum(4,5))
#     # li = [7,4,8,9,11,10,-3,-5,10]
#     # result = list(map(lambda x:x**2,li))
#     # print(f" func map: {result}")
#     #
#     # result = list(filter(lambda x:x%2==0,li))
#     # print(f" func filter: {result}")
#     #
#     # positive_or_neg = lambda num: "positive or zero" if num>=0 else "negative"
#     # print(positive_or_neg(-10))
#     # print(positive_or_neg(10))
#     # print(positive_or_neg(0))
#     #
#     # test_func = lambda *arg: arg[0]*3
#     # print(test_func(5,6,8,3,8,0))
#     #
#     # test_func = lambda **arg: arg.values()
#     # print(test_func(name="Bob", age=18))
#     #show_message()
#
# if __name__ == '__main__':
#     main()
#
#
# def is_negative(num):
#     return num<0
#
# def my_decorator(func):
#     def wrapper():
#         print("Start text")
#         func()
#         print("End text")
#     return wrapper
#
# @my_decorator
# def show_message():
#     print("Hi Python")
#MRO (C3 Linearization)
#Mixin
#iterators
#MVC/MVT (Flask)
import json


#MRO - Method Resolution Order (C3 Лінеарізація)

# class A3:
#     def __init__(self):
#         print("Init A3")
#         super().__init__()
# class A2(A3):
#         def __init__(self):
#             print("Init A2")
#             super().__init__()
# class A1(A2):
#     def __init__(self):
#         print("Init A1")
#         super().__init__()
# class A(A1):
#     def __init__(self):
#         print("Init A")
#         super().__init__()
#
# class B3:
#     def __init__(self):
#         print("Init B3")
#         super().__init__()
#
# class B2(B3):
#     def __init__(self):
#         print("Init B2")
#         super().__init__()
#
# class B1(B2):
#     def __init__(self):
#         print("Init B1")
#         super().__init__()
#
# class B(B1):
#     def __init__(self):
#         print("Init B")
#         super().__init__()
#
# class C(A1,B,A2):
#     def __init__(self):
#         print("Init C")
#         super().__init__()
#
# print(C.mro()) # C B B1 B2 B3 A A1 A2 A3 object
# # print(C.__mro__)


#Mixin - це клас
# class JsonSerializerMixin():
#     import json
#     def to_json(self):
#         return json.dumps(self.__dict__, default=str, ensure_ascii=False)
#
#
# class TimeMixin:
#     def __init__(self, *args,**kwargs):
#         super().__init__(*args,**kwargs)
#         from datetime import datetime
#         self.created_at = datetime.now()
#
# class User(JsonSerializerMixin, TimeMixin):
#     def __init__(self, username: str):
#         super().__init__()
#         self.username = username
#
# u = User("Олександр")
# print(u.to_json())

# def test(*args):
#     print(args)
#
# def test2(*args, **kwargs):
#     print(kwargs)
#
# test2(4,6,7,9,name="Alex", age= 30)
# test(5,7,8,9,3)
# test()
# test(1,3)








# class LoggingMixin:
#     def log(self, message):
#         print(f"[LOG] {message}")
#
# class User(LoggingMixin):
#     def __init__(self, name):
#         self.name = name
#
#     def login(self):
#         print(f"{self.name} logged in")
#         self.log(f"{self.name} logged in")
#
# user = User("Alexander")
# user.login()
# user.log("Login successful")





class Group:
    i = 0
    def __init__(self,students=None):
        self._students = students
    def __iter__(self):
        return self
    def __next__(self):
        if self.i==len(self._students):
            raise StopIteration
        student = self._students[self.i]
        self.i = self.i+1
        return student

group = Group(['Alex', 'Bob', 'Egor'])
for student in group:
    print(student)







