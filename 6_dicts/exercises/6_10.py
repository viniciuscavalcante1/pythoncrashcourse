"""
6.10 Números favoritos:

Modifique seu programa do Exercício 6.2 (página 138)
para que cada pessoa possa ter mais de um número favorito.
Depois, exiba o nome de cada pessoa com seus números favoritos.
"""

favorite_numbers = {'Ben': [7, 7], 'Vi': [12, 12], 'Clara': [1, 1], 'Socorro': [13, 13], 'Bru': [8, 8]}

for k, v in favorite_numbers.items():
    print(f'{k}: {v}')
