"""
5.5 Cores alienígenas #3: Converta sua sequência if-else do Exercício 5.4 em uma sequência if-elif-else.

Se o alienígena for verde, exiba uma afirmação de que o jogador ganhou 5 pontos.
Se o alienígena for amarelo, exiba uma afirmação de que o jogador ganhou 10 pontos.
Se o alienígena for vermelho, exiba uma afirmação de que o jogador ganhou 15 pontos.
Escreva três versões desse programa,
assegurando que cada afirmação exibida seja correspondente à cor adequada do alienígena.
"""

alien_color = 'green'

if alien_color == 'green':
    print('You won 5 points for shooting an alien!')
elif alien_color == 'yellow':
    print('You won 10 points for shooting an alien!')
elif alien_color == 'red':
    print('You won 15 points for shooting an alien!')

alien_color = 'yellow'

if alien_color == 'green':
    print('You won 5 points for shooting an alien!')
elif alien_color == 'yellow':
    print('You won 10 points for shooting an alien!')
elif alien_color == 'red':
    print('You won 15 points for shooting an alien!')

alien_color = 'red'

if alien_color == 'green':
    print('You won 5 points for shooting an alien!')
elif alien_color == 'yellow':
    print('You won 10 points for shooting an alien!')
elif alien_color == 'red':
    print('You won 15 points for shooting an alien!')
