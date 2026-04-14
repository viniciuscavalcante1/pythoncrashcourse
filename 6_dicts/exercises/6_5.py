"""
6.5 Rios:
Crie um dicionário contendo os três principais rios e o país por onde cada rio passa.
Um par chave-valor pode ser 'nile': 'egypt'.

Use um loop para exibir uma frase sobre cada rio, como: O Nilo atravessa o Egito.
Use um loop para exibir o nome de cada rio incluído no dicionário.
Use um loop para exibir o nome de cada país incluído no dicionário.
"""

rivers = {
    'nile': 'egypt',
    'amazonas': 'brazil',
    'yangtze': 'china',
}

for river, country in rivers.items():
    print(f"The {river.title()} is a river in {country.title()}.")

for river in rivers.keys(): print(river.title())

for country in rivers.values(): print(country.title())