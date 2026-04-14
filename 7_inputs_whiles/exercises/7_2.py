"""
7.2 Reservas em restaurante:

Crie um programa que pergunte quantos lugares em uma mesa o usuário precisa.

Se a resposta for mais de oito, exiba uma mensagem informando que é necessário aguardar por uma mesa.

Caso contrário, informe que a mesa já está disponível.
"""

seats = int(input("Diga quantos lugares você precisa: "))

if seats > 8:
    print("É necessário aguardar por uma mesa...")
else:
    print("A mesa já está disponível!")