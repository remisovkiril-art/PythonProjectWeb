class Money:
    def __init__(self, whole, cents):
        self.whole = whole
        self.cents = cents
        self.normalize()

    def normalize(self):
        self.whole += self.cents // 100
        self.cents = self.cents % 100

    def set_whole(self, whole):
        self.whole = whole

    def set_cents(self, cents):
        self.cents = cents
        self.normalize()

    def show_amount(self):
        print(f"{self.whole}.{self.cents:02d}")


class Product(Money):
    def __init__(self, name, whole, cents):
        super().__init__(whole, cents)
        self.name = name

    def show_product(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.whole}.{self.cents:02d}")

    def reduce_price(self, amount):
        total = self.whole * 100 + self.cents
        total -= amount

        if total < 0:
            total = 0

        self.whole = total // 100
        self.cents = total % 100


money = Money(10, 75)

print("Money amount:")
money.show_amount()

money.set_whole(15)
money.set_cents(150)

print("Updated money amount:")
money.show_amount()

product = Product("Coffee", 25, 50)

print("Product information:")
product.show_product()

product.reduce_price(300)

print("Reduced price:")
product.show_product()
