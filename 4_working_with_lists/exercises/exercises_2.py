"""
4.3 Contando até vinte: Use um loop for para exibir os números de 1 a 20, todos juntos.
"""

print(list(range(1, 21)))

"""
4.4 Um milhão: Crie uma lista com números de um a um milhão e, em seguida, utilize um loop for para exibi-los. (Se a saída estiver demorando muito, interrompa-a pressionando CTRL+C ou fechando a janela de saída.)
"""

million = list(range(1, 1000001))
for number in million: print(number)

"""
4.5 Somando um milhão: crie uma lista com números de um a um milhão e, em seguida, use min() e max() a fim de garantir que sua lista realmente comece em um e termine em um milhão. Além disso, use a função sum() para ver a rapidez com que o Python pode efetuar a soma de um milhão de números.
"""

print(min(million))
print(max(million))
print(sum(million))

"""
4.6 Números ímpares: Use o terceiro argumento da função range() para criar uma lista com números ímpares de 1 a 20. Use o loop for para exibir cada número.
"""

odds = list(range(1, 20, 2))
for odd in odds: print(odd)

"""
4.7 Três: Crie uma lista dos múltiplos de 3, de 3 a 30. Use um loop for para exibir os números em sua lista.
"""

multiple_of_3 = list(range(3, 31, 3))
for multiple in multiple_of_3: print(multiple)

"""
4.8 Cubos: Um número elevado à terceira potência é chamado de cubo. Por exemplo, no Python, o cubo de 2 é escrito como 2**3. Escreva uma lista dos primeiros 10 cubos (ou seja, o cubo de cada número inteiro de 1 a 10) e use um loop for para exibir o valor de cada cubo.
"""

cubes = [x ** 3 for x in range(1, 11)]
for cube in cubes: print(cube)

"""
4.9 Cube Comprehension: Use uma list comprehension para gerar uma lista dos primeiros 10 cubos.
"""

cubes = [x ** 3 for x in range(1, 11)]
for cube in cubes: print(cube)
