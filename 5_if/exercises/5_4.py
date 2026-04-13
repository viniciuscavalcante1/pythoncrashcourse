"""
5.4 Cores de alienígenas #2: Escolha uma cor para um alienígena, como no Exercício 5.3,
e escreva uma sequência if-else.

Se a cor do alienígena for verde,
exiba uma afirmação de que o jogador acabou de ganhar 5 pontos por abrir fogo contra um alienígena.
Se a cor do alienígena não for verde,
exiba uma afirmação de que o jogador acabou de ganhar 10 pontos.
Escreva uma versão desse programa que execute o bloco if e outra que execute o bloco else.
"""

alien_color = 'green'

if alien_color == 'green':
    print('You won 5 points for shooting an alien!')
else:
    print('You won 10 points.')

alien_color = 'yellow'

if alien_color == 'green':
    print('You won 5 points for shooting an alien!')
else:
    print('You won 10 points.')
