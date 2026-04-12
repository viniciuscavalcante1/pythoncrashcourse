"""
4.11 Minhas pizzas, suas pizzas: Comece com o programa do Exercício 4.1 (página 90). Faça uma cópia da lista de pizzas e a nomeie como friend_pizzas. Em seguida, siga as etapas:

Adicione uma pizza nova à lista original.
Adicione uma pizza diferente à lista friend_pizzas.
Prove que tem duas listas separadas. Exiba a mensagem: Minhas pizzas favoritas são:. E, em seguida, use um loop for para exibir a primeira lista. Exiba a mensagem: Minhas pizzas favoritas são:. E, em seguida, use um loop for para exibir a segunda lista. Garanta que cada pizza nova seja armazenada na lista adequada.
"""

pizzas = ['Marguerita', 'Frango com catupiry', 'Ribs']
friend_pizzas = pizzas[:]

pizzas.append('Peito de peru')
friend_pizzas.append('Palmito')

pizzas_str = ""
for pizza in pizzas:
    if pizzas_str != "":
        if pizza == pizzas[-1]:
            pizzas_str = pizzas_str + " e " + pizza
            break
        pizzas_str = pizzas_str + ", " + pizza
    else:
        pizzas_str = pizzas_str + pizza

pizzas_friend_str = ""
for pizza in friend_pizzas:
    if pizzas_friend_str != "":
        if pizza == friend_pizzas[-1]:
            pizzas_friend_str = pizzas_friend_str + " e " + pizza
            break
        pizzas_friend_str = pizzas_friend_str + ", " + pizza
    else:
        pizzas_friend_str = pizzas_friend_str + pizza

print(f"Minhas pizzas favoritas são {pizzas_str}, enquanto as do meu amigo são {pizzas_friend_str}")