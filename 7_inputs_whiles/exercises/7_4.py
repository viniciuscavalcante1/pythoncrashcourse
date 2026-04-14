"""
7.4 Ingredientes de pizza:

Escreva um loop que solicite ao usuário uma série de ingredientes de pizza até que ele forneça o valor 'quit'.

À medida que cada ingrediente é fornecido, exiba uma mensagem informando que esses ingredientes
estão sendo adicionados à pizza.
"""

toppings = []
while True:
    topping = input("Escreva um ingrediente para a pizza (q pra sair): ")

    if topping == "q":
        if toppings:
            print(f"A pizza ficou com {len(toppings)} ingredientes: {", ".join(toppings)}")
        else:
            print("SÓ MASSA!")
        break
    toppings.append(topping)
    print(f"Irei adicionar {topping} à pizza!")