class Dog:
    """models a dog"""

    def __init__(self, name, age):
        """constructor method that starts name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """sit method"""
        print(f"{self.name} is sitting.")

    def roll_over(self):
        """roll over method"""
        print(f"{self.name} rolled over.")

my_dog = Dog('Linda', 10)
print(f'{my_dog.name} is {my_dog.age}.')
my_dog.sit()
my_dog.roll_over()

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kilometers on it.")

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer(self, kilometrage):
        if kilometrage >= self.odometer_reading:
            self.odometer_reading = kilometrage
        else:
            print("you can't roll it back!")

    def increment_odometer(self, kilometers):
        if kilometers > 0:
            self.odometer_reading += kilometers
        else:
            print("you can't roll it back!")

my_car = Car(make='audi', model='a4', year=2024)
print(my_car.get_descriptive_name())
my_car.read_odometer()

my_car.odometer_reading = 10
my_car.read_odometer() # 10

my_car.update_odometer(kilometrage=20)
my_car.read_odometer() # 20

my_car.increment_odometer(kilometers=10)
my_car.read_odometer() # 30

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_byd = ElectricCar('byd', 'dolphin', 2025)
print(my_byd.get_descriptive_name())