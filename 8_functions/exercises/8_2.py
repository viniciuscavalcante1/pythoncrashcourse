"""
8.2 Livro favorito:

Escreva uma função chamada favorite_book() que aceite um parâmetro, title.
A função deve exibir uma mensagem como: Um dos meus livros favoritos é Alice no País das Maravilhas.
Chame a função e lembre-se de incluir o título de um livro como argumento na chamada da função.
"""

def favorite_book(title):
    print(f"Um dos meus livros favoritos é {title.title()}")

favorite_book("O nome do vento")