"""
3.8 Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que você gostaria de conhecer. • Armazene esses locais em uma lista. Verifique se ela não está em ordem alfabética.

Exiba sua lista na ordem original. Não se preocupe em exibir a lista ordenadamente; basta exibi-la como uma lista crua do Python. • Use sorted() para exibir sua lista em ordem alfabética, sem alterar a lista original. • Mostre que sua lista ainda está na ordem original exibindo-a. • Use o sorted() para exibir sua lista em ordem alfabética reversa, sem alterar a ordem original dela. • Demonstre que sua lista ainda está na ordem original exibindo-a mais uma vez. • Use o reverse() para alterar a ordem de sua lista. Exiba essa lista para mostrar que sua ordem foi alterada. • Use o reverse() para alterar a ordem de sua lista novamente. Exiba-a a fim de mostrar que voltou à ordem original. • Use o sort() para alterar sua lista para que ela seja armazenada em ordem alfabética. Exiba a lista para mostrar que sua ordem foi alterada. • Use sort() para alterar sua lista, de modo que ela seja armazenada em ordem alfabética inversa. Exiba a lista para mostrar que sua ordem foi alterada.

"""

places = ['Chile', 'Peru', 'Argentina', 'França', 'Japão', 'Inglaterra', 'Estados Unidos', 'Itália', 'Portugal',
          'Espanha', 'Alemanha']

print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

"""
3.9 Convidados para o jantar: Recorra a um dos programas dos exercícios 3.4 a 3.7 (páginas 75-76), e use len() para exibir uma mensagem indicando o número de pessoas que você está convidando para jantar.

Matthes, Eric. Curso Intensivo de Python - 3ª edição: Uma Introdução Prática e Baseada em Projetos à Programação (Portuguese Edition) (p. 99). (Function). Kindle Edition. 
"""

print(f"Quero conhecer {len(places)} lugares!")

"""
3.10 Funções: Pense em coisas que você conseguiria armazenar em uma lista. Por exemplo, você pode criar uma lista de montanhas, rios, países, cidades, idiomas, ou qualquer outra coisa que quiser. Crie um programa com uma lista contendo esses itens e, em seguida, use cada função apresentada neste capítulo, pelo menos, uma vez.

Matthes, Eric. Curso Intensivo de Python - 3ª edição: Uma Introdução Prática e Baseada em Projetos à Programação (Portuguese Edition) (p. 99). (Function). Kindle Edition. 
"""

gadgets = ['Galaxy S24', 'Galaxy Watch 7', 'MacBook Air M2', 'Logitech Keyboard', 'Logitech Mouse']
print(gadgets[0])
print(gadgets[-1])
gadgets[0] = 'Samsung Galaxy S24'
gadgets.append('Charger')
gadgets.insert(0, 'Monitor')
del gadgets[0]
popped = gadgets.pop()
popped = gadgets.pop(3)
gadgets.remove('Logitech Mouse')
gadgets.sort()
gadgets.sort(reverse=True)
print(sorted(gadgets))
print(sorted(gadgets, reverse=True))
gadgets.reverse()
gadgets.reverse()
print(len(gadgets))