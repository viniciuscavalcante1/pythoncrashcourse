"""
8.3 Camiseta:

Crie uma função chamada make_shirt() que aceita um tamanho e o texto que deve ser estampado na camiseta.
A função deve exibir uma frase resumindo o tamanho da camiseta e a mensagem estampada nela.

Chame a função uma vez usando argumentos posicionais para criar uma camiseta.
Chame a função uma segunda vez usando argumentos nomeados.
"""

def make_shirt(size, text):
    print(f"Frase: {text}. Tamanho: {size}")

make_shirt("G", "Hello World")
make_shirt(size="G", text="Hello World")