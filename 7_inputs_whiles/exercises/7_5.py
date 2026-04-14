"""
7.5 Ingressos de cinema:

Um cinema cobra preços de ingressos diferentes, dependendo da idade da pessoa.

Se a pessoa for menor de 3 anos, o ingresso é gratuito;
se tiver entre 3 e 12 anos, o ingresso custa US$10;
e caso tenha mais de 12 anos, o ingresso custa US$15.

Escreva um loop que pergunte a idade dos usuários e, em seguida, informe o preço do ingresso do cinema.
"""

while True:
    age = int(input("Digite sua idade: "))

    if age < 3:
        cost = "gratuito"
    elif 3 <= age <= 12:
        cost = "US$10"
    else:
        cost = "US$15"

    print(f"O ingresso é {cost}")