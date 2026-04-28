# 9.2 Três restaurantes: Comece com sua classe do Exercício 9.1. Crie três instâncias
# diferentes da classe e chame describe_restaurant() para cada instância.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}. Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open.")

restaurant = Restaurant(restaurant_name='Guaco', cuisine_type='Mexican')
restaurant.describe_restaurant()

restaurant_2 = Restaurant(restaurant_name='Barakah', cuisine_type='Arabic')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant(restaurant_name='Gendai', cuisine_type='Japanese')
restaurant_3.describe_restaurant()
