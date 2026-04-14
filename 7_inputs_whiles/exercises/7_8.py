"""
7.8 Lanchonete:

Crie uma lista chamada sandwich_orders e a preencha com o nome de diversos sanduíches.
Depois, crie uma lista vazia chamada finished_sandwiches.
Percorra a lista de pedidos de sanduíches com um loop e exiba uma mensagem para cada pedido,
como: Seu lanche de atum está pronto.
Conforme cada sanduíche é preparado, passe-os para a lista de sanduíches prontos.
Após todos os sanduíches terem sido preparados, exiba uma mensagem enumerando cada um deles.
"""

sandwich_orders = ['pastrami', 'cheese', 'tapioca']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Seu {sandwich} está pronto!")
    finished_sandwiches.append(sandwich)

for i, sandwich in enumerate(finished_sandwiches):
    print(f"{i} - {sandwich}")