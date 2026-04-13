"""
5.2 Mais testes condicionais: não é necessário restringir o número de testes a 10.
Caso queira executar mais comparações, escreva mais testes e os adicione a conditional_tests.py.
Gere, pelo menos, um resultado True e um False para cada condição a seguir:

Testes com operadores de igualdade e de diferença com strings.
Testes usando o método lower().
Testes numéricos com operadores de igualdade e de diferença, maior e menor que, maior ou igual que e menor ou igual a.
Testes com as palavras reservadas and e or.
Testes para averiguar se um valor consta em uma lista.
Testes para averiguar se um valor não consta em uma lista.
"""

# igualdade
print('a' == 'a')
print('a' == 'b')

# desigualdade
print('a' != 'a')
print('a' != 'b')

# lower
print('A'.lower() == 'a'.lower())
print('B'.lower() != 'b'.lower())

# numeric
print(1 == 1)
print(1 == 2)
print(2 > 1)
print(2 > 5)
print(1 < 2)
print(5 < 2)
print(5 >= 5)
print(5 >= 6)
print(5 <= 5)
print(5 <= 4)

# and/or
print((5 > 1) and (5 < 10))
print((5 < 1) and (5 > 10))
print((5 > 1) or (5 > 10))
print((5 < 1) or (5 > 10))

# in
colors = ['black', 'white']
print('white' in colors)
print('yellow' in colors)

# not in
print('yellow' not in colors)
print('white' not in colors)