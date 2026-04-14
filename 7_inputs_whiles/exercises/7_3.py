"""
7.3 Múltiplos de dez:

Solicite ao usuário um número e informe se o número é múltiplo de 10 ou não.
"""

number = int(input("Por favor, diga um número: "))
multiple_10 = number % 10 == 0

if multiple_10:
    print("É múltiplo de 10!")
else:
    print("Não é múltiplo de 10")