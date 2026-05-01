# 9.9 Trocar bateria: Utilize a versão final do electric_car.py dessa seção. Adicione um
# método à classe Battery chamado upgrade_battery(). Esse método deve verificar o tamanho
# da bateria e definir a capacidade como 65, caso necessário. Crie um carro elétrico com
# um tamanho default de bateria, chame get_range() uma vez e, depois, chame get_range()
# uma segunda vez, após atualizar a bateria. Você deve ver aumento no alcance de distância
# do carro.

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

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"The battery size is {self.battery_size}")

    def upgrade_battery(self):
        if self.battery_size <= 65:
            self.battery_size = 65

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank.")


my_byd = ElectricCar('byd', 'dolphin', 2025)
my_byd.battery.describe_battery()

print(my_byd.get_descriptive_name())