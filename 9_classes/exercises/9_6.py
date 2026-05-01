# 9.6 Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva uma classe
# chamada IceCreamStand que herde da classe Restaurant do Exercício 9.1 ou Exercício 9.4.
# Adicione um atributo chamado flavors que armazene uma lista de sabores de sorvete.
# Escreva um método que exiba esses sabores. Crie uma instância a partir de IceCreamStand
# e chame esse método.

from restaurant9_4 import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name=restaurant_name, cuisine_type=cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print(self.flavors)

stand = IceCreamStand('Bacio', 'Ice Cream', ['strawberry', 'grape'])
stand.show_flavors()