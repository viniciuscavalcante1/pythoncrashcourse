"""
7.6 Três saídas:

Crie diferentes versões do Exercício 7.4 ou 7.5 que executem cada uma das seguintes tarefas, pelo menos uma vez:

Use um teste condicional na instrução while para interromper o loop.
Use uma variável active para controlar o tempo que o loop é executado.
Use uma instrução break para sair do loop quando o usuário inserir o valor 'quit'.
"""

toppings = []
active = True
while active:
    topping = input("Escreva um ingrediente para a pizza (q pra sair): ")

    if topping == "q":
        if toppings:
            print(f"A pizza ficou com {len(toppings)} ingredientes: {", ".join(toppings)}")
        else:
            print("SÓ MASSA!")
        active = False
        break
    toppings.append(topping)
    print(f"Irei adicionar {topping} à pizza!")