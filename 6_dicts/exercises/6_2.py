"""
6.2 Números favoritos:
Use um dicionário para armazenar os números favoritos das pessoas.
Pense em cinco nomes e os utilize como chaves em seu dicionário.
Pense em um número favorito para cada pessoa e armazene cada um como um valor em seu dicionário.
Exiba o nome de cada pessoa e seu número favorito.
Para que tudo fique ainda mais divertido, pergunte a alguns amigos e obtenha alguns dados reais para o seu programa.
"""

favorite_numbers = {'Ben': 7, 'Vi': 12, 'Clara': 1, 'Socorro': 13, 'Bru': 8}

for k, v in favorite_numbers.items():
    print(f'{k}: {v}')
