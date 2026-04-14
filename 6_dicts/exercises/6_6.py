"""
6.6 Pesquisa:
Use o código de favorite_languages.py (página 135).
Crie uma lista de pessoas que deveriam participar da pesquisa de linguagens favoritas.
Inclua alguns nomes que já estão no dicionário e outros que não estão.

Percorra com um loop a lista de pessoas que devem participar da pesquisa.
Se já tiverem respondido, exiba uma mensagem agradecendo a resposta.
Se ainda não tiverem respondido, exiba uma mensagem as convidando a participar.
"""

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'ruby',
}

people_that_should_join = ['vini', 'jen', 'josh']
for name in people_that_should_join:
    if name in favorite_languages.keys():
        print(f"{name}, obrigado por participar!")
    else:
        print(f"{name}, por favor, participe da pesquisa!")

