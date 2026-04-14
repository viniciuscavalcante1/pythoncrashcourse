"""
7.9 Sem pastrami:

Usando a lista sandwich_orders do Exercício 7.8,
assegure-se de que o sanduíche 'pastrami' apareça na lista pelo menos três vezes.
Faça mais um código perto do início de seu programa,
exibindo uma mensagem que informe que a lanchonete está sem pastrami e,
em seguida, use um loop while para remover todas as ocorrências de 'pastrami' em sandwich_orders.
Faça questão de que nenhum sanduíche de pastrami acabe em finished_sandwiches.
"""

sandwich_orders = ['pastrami', 'cheese', 'tapioca', 'pastrami', 'pastrami']
finished_sandwiches = []

print('Infelizmente estamos sem pastrami!')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Seu {sandwich} está pronto!")
    finished_sandwiches.append(sandwich)

for i, sandwich in enumerate(finished_sandwiches):
    print(f"{i} - {sandwich}")