import json

class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class JsonMixin:
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "price": self.price
        })

class DiscountMixin:
    def apply_discount(self, percent):
        self.price = self.price - self.price * percent / 100
        return self.price

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ProductManager(Product, LoggingMixin, JsonMixin, DiscountMixin):
    def __init__(self, name, price):
        super().__init__(name, price)


