"""
6.11 Cidades:

Crie um dicionário chamado cities.

Utilize o nome de três cidades como chaves de seu dicionário.

Crie um dicionário de informações sobre cada cidade e inclua o país em que a cidade está,
sua população aproximada e um fato sobre essa cidade.

O nome das chaves para o dicionário de cada cidade devem ser alguma coisa como country, population e fact.

Exiba o nome de cada cidade e todas as informações que você armazenou a respeito.
"""

cities = {
    'São Paulo': {
        'país': 'Brasil',
        'população': '+1MI',
        'fato': 'cidade da garoa'
    },
    'Tupanatinga': {
        'país': 'Brasil',
        'população': '+10',
        'fato': 'quase todo mundo se conhece'
    }
}

for city, city_info in cities.items():
    print(f"A cidade {city} está no {city_info['país']}, com população aproximada de {city_info['população']} de pessoas."
          f"Ela é conhecida por esse fato: {city_info['fato']}")