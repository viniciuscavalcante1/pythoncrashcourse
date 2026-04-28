"""
8.8 Álbuns de usuários:

Comece com seu programa do Exercício 8.7.
Escreva um loop while que possibilite aos usuários inserir o artista e o título de um álbum.
Após receber essas informações, chame make_album() com a entrada do usuário e exiba o dicionário criado.
Não se esqueça de incluir um valor de saída no loop while.
"""

def make_album(artist, title, n_musics=None):
    album = {
        'artist': artist,
        'title': title
    }

    if n_musics:
        album['n_musics'] = n_musics

    return album


print(make_album('artist 1', 'title 1'))
print(make_album('artist 2', 'title 2'))
print(make_album('artist 3', 'title 3', 12))
