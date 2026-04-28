"""
8.7 Álbum:

Escreva uma função chamada make_album() que crie um dicionário representando um álbum de música.
A função deve ter o nome de um artista e o título de álbum,
e deve retornar um dicionário com essas duas informações.
Utilize a função para criar três dicionários representando álbuns distintos.
Exiba cada valor de retorno para mostrar que os dicionários estão armazenando
adequadamente as informações do álbum.

Use None para adicionar um parâmetro opcional ao make_album() que possibilite
armazenar o número de músicas em um álbum.
Se a linha chamadora incluir um valor para o número de músicas,
adicione esse valor ao dicionário do álbum.
Crie, pelo menos, uma nova chamada de função que inclua o número de músicas em um álbum.
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
