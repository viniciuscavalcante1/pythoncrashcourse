toppings = ['Coco', 'Banana', 'Granola']
available_toppings = ['Coco', 'Banana', 'Granola', 'Leite Condensado', 'Leite Ninho']

if toppings:
    for topping in toppings:
        if topping == 'Coco':
            print('Desculpe, estamos sem coco!')
        elif topping in available_toppings:
            print(f"Adicionando {topping}!")
        else:
            print(f"Desculpe, não temos {topping}")
else:
    print("Você tem certeza que não quer adicionar nenhum topping?")
print('Seu açaí está pronto!')
