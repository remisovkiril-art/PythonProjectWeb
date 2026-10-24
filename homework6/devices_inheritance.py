class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Power: {self.power} W")


class CoffeeMachine(Device):
    def make_coffee(self):
        print("Coffee is ready")


class Blender(Device):
    def blend(self):
        print("Blending products")


class MeatGrinder(Device):
    def grind_meat(self):
        print("Grinding meat")


coffee_machine = CoffeeMachine("Philips", "Series 2200", 1500)
blender = Blender("Bosch", "SilentMixx", 600)
meat_grinder = MeatGrinder("Moulinex", "ME306", 1400)

print("Coffee Machine:")
coffee_machine.show_info()
coffee_machine.make_coffee()

print("Blender:")
blender.show_info()
blender.blend()

print("Meat Grinder:")
meat_grinder.show_info()
meat_grinder.grind_meat()
