"""
Crie uma lista com os nomes de 5 cidades que você gostaria de visitar.
Use um loop for para exibir uma frase do tipo "Eu adoraria visitar [cidade]!" para cada uma.
"""

cities = ['Tóquio', 'Santiago', 'Paris', 'Londres', 'Nova Iorque']
for city in cities: print(f"Eu adoraria visitar {city}!")

"""
Use range() para gerar e imprimir a tabuada de um número qualquer (ex: tabuada do 7, de 1 a 10).
"""

number = 7
for i in range(1, 11):
    print(f"{i} * {number} = {i * number}")

"""
Crie uma lista de números de 1 a 20. Use um loop para imprimir apenas os números divisíveis por 3.
"""

numbers = range(1, 21)
numbers_3 = [number for number in numbers if number % 3 == 0]
for number in numbers_3: print(number)

"""
Usando list comprehension, crie uma lista com os cubos dos números de 1 a 15.
"""

numbers = [number ** 3 for number in range(1, 16)]
print(numbers)

"""
Crie uma list comprehension que gere uma lista apenas com as palavras que têm mais 
de 5 letras a partir de uma lista de palavras qualquer.
"""

words = ['Tio', 'Vi', 'Garrafa', 'Livro', 'Mesa', 'Computador', 'Escrever']
words_with_more_than_five_letters = [word for word in words if len(word) > 5]
print(words_with_more_than_five_letters)

"""
Dada uma lista com 10 elementos, imprima separadamente: 
os 3 primeiros, os 3 últimos, e os elementos do meio (posições 3 a 6).
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[:3])
print(numbers[-3:])
print(numbers[3:6])

"""
Use fatiamento para inverter uma lista.
"""

numbers_inverted = numbers[-1::-1]
print(numbers_inverted)

"""
Crie uma lista de filmes favoritos. Faça uma cópia dela. 
Adicione um filme diferente em cada lista e prove que são independentes.
"""

favourite_movies = ["Interstellar", "Inception"]
favourite_movies_2 = favourite_movies[:]
favourite_movies.append('Avatar')
favourite_movies_2.append('Dune')
print(favourite_movies, favourite_movies_2)

"""
Defina uma tupla com as coordenadas de um ponto (x, y, z). 
Tente alterar um valor e observe o erro. Depois, "sobrescreva" a tupla inteira com novas coordenadas.
"""

coords = (10, 10, 10)
# coords[0] = 20
coords = (20, 10, 10)
print(coords)