# 9.1 Restaurante: Crie uma classe chamada Restaurant. O método __init__() para
# Restaurant deve armazenar dois atributos: restaurant_name e cuisine_type. Crie um
# método chamado describe_restaurant() que exiba essas duas informações e um método
# chamado open_restaurant() que exiba uma mensagem sinalizando que o restaurante está aberto.
# Crie uma instância chamada restaurant a partir da sua classe. Exiba os dois atributos
# individualmente e, em seguida, chame ambos os métodos.

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name}. Cuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print("The restaurant is open.")

restaurant = Restaurant(restaurant_name='Guaco', cuisine_type='Mexican')
print(f'Restaurant name: {restaurant.restaurant_name}')
print(f'Cuisine type: {restaurant.cuisine_type}')

restaurant.describe_restaurant()
restaurant.open_restaurant()
