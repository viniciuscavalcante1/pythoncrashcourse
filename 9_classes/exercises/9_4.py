# 9.4 Pessoas atendidas: Comece com o seu programa do Exercício 9.1. Adicione um atributo
# chamado number_served com um valor default de 0. Crie uma instância chamada restaurant
# a partir dessa classe. Exiba o número de clientes que o restaurante atendeu e, em seguida,
# altere este valor e o exiba novamente.
# Adicione um método chamado set_number_served() que possibilita definir o número de clientes
# atendidos. Chame esse método com um novo número e exiba mais uma vez o valor.
# Adicione um método chamado increment_number_served(), o qual possibilita aumentar o número
# de clientes atendidos. Chame esse método com qualquer número que quiser e que possa
# representar quantos clientes foram atendidos em, digamos, um dia de atividade comercial.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number):
        self.number_served += number

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}. Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open.")

restaurant = Restaurant(restaurant_name='Guaco', cuisine_type='Mexican')
print(f'Restaurant name: {restaurant.restaurant_name}')
print(f'Cuisine type: {restaurant.cuisine_type}')

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("Number served: ", restaurant.number_served)
restaurant.number_served = 10
print("Number served: ", restaurant.number_served)

restaurant.set_number_served(20)
print("Number served: ", restaurant.number_served)

restaurant.increment_number_served(10)
print("Number served: ", restaurant.number_served)
