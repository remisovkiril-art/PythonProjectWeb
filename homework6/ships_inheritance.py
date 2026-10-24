class Ship:
    def __init__(self, name, displacement, speed):
        self.name = name
        self.displacement = displacement
        self.speed = speed

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Displacement: {self.displacement} tons")
        print(f"Speed: {self.speed} knots")


class Frigate(Ship):
    def patrol(self):
        print("Frigate is patrolling")


class Destroyer(Ship):
    def defend(self):
        print("Destroyer is defending the fleet")


class Cruiser(Ship):
    def launch_mission(self):
        print("Cruiser is carrying out a mission")


frigate = Frigate("HMS Frigate", 4000, 30)
destroyer = Destroyer("HMS Destroyer", 8000, 32)
cruiser = Cruiser("HMS Cruiser", 10000, 28)

print("Frigate:")
frigate.show_info()
frigate.patrol()

print("\nDestroyer:")
destroyer.show_info()
destroyer.defend()

print("\nCruiser:")
cruiser.show_info()
cruiser.launch_mission()
