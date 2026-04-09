"""
Exercício 1 — Playlist de músicas
Crie uma lista com 5 músicas que você gosta. Depois:

Mostre a terceira música usando seu índice
Mostre a última música usando índice negativo
Use uma f-string para exibir: "Agora tocando: [primeira música]"
"""

playlist = ["Through the Fire and Flames", "Welcome to the Jungle", "Knights of Cydonia", "Even Flow", "One"]
print(f"A terceira música é {playlist[2]}")
print(f"A última música é {playlist[-1]}")
print(f"Agora tocando: {playlist[0]}")

"""
Exercício 2 — Lista de compras dinâmica
Comece com uma lista de compras: ['arroz', 'feijão', 'café']. Depois:

Adicione 'leite' ao final
Adicione 'pão' no início da lista
Remova 'café' pelo nome
Exiba a lista final e quantos itens ela tem
"""

groceries = ['arroz', 'feijão', 'café']
groceries.append('leite')
groceries.insert(0, 'pão')
groceries.remove('café')
print(f"A lista atual é {groceries}, com {len(groceries)} itens!")


"""
Exercício 3 — Ranking de jogos
Crie uma lista com 6 jogos. Depois:

Exiba a lista original
Exiba a lista em ordem alfabética sem alterar a original
Agora ordene a lista permanentemente em ordem alfabética reversa
Exiba a lista para confirmar
"""

games = ['World of Warcraft', 'League of Legends', 'Super Mario', 'FIFA', 'Legends of Zelda', 'Cookie Clicker']
print(games)
print(sorted(games))
games.sort(reverse=True)
print(games)

"""
Exercício 4 — Fila do cinema
Crie a lista: ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eva']. Simule:

Bruno desistiu — remova ele da fila
Eva foi chamada por um amigo na frente — tire ela do final e guarde numa variável
Coloque Eva na posição 1
'Felipe' chegou por último
Exiba a fila final e uma mensagem dizendo quem furou a fila
"""

queue = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eva']
queue.remove('Bruno')
eva = queue.pop()
queue.insert(0, eva)
queue.append('Felipe')
print(f'A fila é {queue}, e a {eva} furou a fila!')

"""
Exercício 5 — Erro proposital
Crie uma lista com exatamente 4 elementos. Depois:

Tente acessar um índice que não existe — observe o erro
Corrija o código para acessar o último elemento de forma segura
Tente remover um valor que não está na lista — observe o erro
Comente o código com erro e explique por que aconteceu
"""

elements = [1, 2, 3, 4]
# print(elements[10]) # IndexError: list index out of range
print(elements[-1])
# elements.remove(10) # ValueError: list.remove(x): x not in list
# esses erros aconteceram por que os elementos não estão na lista

"""
Exercício 6 — Desafio: Troca de posições
Crie a lista ['ouro', 'prata', 'bronze']. Sem criar uma nova lista, troque o primeiro e o último elemento de posição. Exiba antes e depois.
"""

metals = ['ouro', 'prata', 'bronze']
print(f'Antes: {metals}')
to_be_first_element = metals.pop()
to_be_last_element = metals.pop(0)

metals.insert(0, to_be_first_element)
metals.append(to_be_last_element)
print(f"Depois: {metals}")