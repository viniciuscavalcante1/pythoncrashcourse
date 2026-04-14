"""
6.8 Animais de estimação:
Crie vários dicionários,
em que cada dicionário representa um animal de estimação diferente.
Em cada dicionário inclua o tipo de animal e o nome do dono.
Armazene esses dicionários em uma lista chamada pets.
Depois, percorra sua lista com um loop e, enquanto faz isso, exiba tudo o que sabe sobre cada animal de estimação.
"""

linda = {
    'tipo': 'cachorra',
    'dono': 'vini'
}

panqueca = {
    'tipo': 'cachorra',
    'dono': 'benjamin'
}

kitkat = {
    'tipo': 'gata',
    'dono': 'benjamin'
}

pets = [linda, panqueca, kitkat]
for pet in pets:
    print(f'O {pet['dono']} tem uma {pet['tipo']}')