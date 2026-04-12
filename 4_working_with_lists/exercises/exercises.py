"""
4.1 Pizzas: Pense em, pelo menos, três tipos que você gosta. Armazene esses nomes de pizza em uma lista e use um loop for para exibir o nome de cada uma. • Modifique seu loop for a fim de que exiba uma frase usando o nome da pizza, em vez de exibir apenas o nome da pizza. Para cada pizza, você deve gerar uma linha de saída com uma simples afirmação como: Gosto de pizza de pepperoni. • Adicione uma linha no final do seu programa, fora do loop for, que ressalte o quanto você gosta de pizza. A saída deve ter três ou mais linhas sobre os tipos de pizza que você gosta e, em seguida, uma frase adicional, como Eu amo pizza!

Matthes, Eric. Curso Intensivo de Python - 3ª edição: Uma Introdução Prática e Baseada em Projetos à Programação (Portuguese Edition) (p. 112). (Function). Kindle Edition.
"""

pizzas = ['Marguerita', 'Frango com catupiry', 'Ribs']
for pizza in pizzas:
    print(f"Eu gosto de pizza de {pizza}")
print("Adoro pizza!")

"""
4.2 Animais: Pense em, pelo menos, três animais diferentes que compartilhem uma característica comum. Armazene o nome desses animais em uma lista e, em seguida, use um loop for para exibir o nome de cada animal.

Modifique seu programa a fim de exibir uma afirmação sobre cada animal, como Um cachorro seria um ótimo animal de estimação (pet).
Adicione uma linha no final do seu programa, indicando o que esses animais compartilham em comum. Você pode exibir uma frase, como Qualquer um desses animais daria um ótimo animal de estimação!
"""

animals = ['cachorro', 'gato', 'tartaruga']
for animal in animals:
    print(f"Um {animal} é um bom animal de astimação.")
print("Qualquer desses animais seriam bons animais de estimação.")