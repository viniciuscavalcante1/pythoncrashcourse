"""
6.7 Pessoas:

comece com o programa escrito para Exercício 6.1 (página 138).
Crie dois dicionários novos representando pessoas diferentes e
armazene todos os três dicionários em uma lista chamada people.
Percorra sua lista de pessoas com um loop. À medida que percorre a lista, exiba tudo o que sabe sobre cada pessoa.
"""

person = {'first_name': 'Benjamin', 'last_name': 'Curti', 'age': 9, 'city': 'Indaiatuba'}
person_2 = {'first_name': 'Clara', 'last_name': 'Curti', 'age': 6, 'city': 'Indaiatuba'}
person_3 = {'first_name': 'Bruna', 'last_name': 'Curti', 'age': 35, 'city': 'Indaiatuba'}

people = [person, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}".title()
    print(f'A pessoa {full_name} tem {person['age']} anos e mora em {person['city']}')
