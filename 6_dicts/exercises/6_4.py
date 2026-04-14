"""
6.4 Glossário 2:
Agora você sabe como percorrer um dicionário com um loop,
limpe o código do Exercício 6.3 (página 138) substituindo sua série de print() por um loop
que percorre as chaves e os valores do dicionário.
Quando tiver certeza de que seu loop funciona,
adicione mais cinco termos Python ao seu glossário.
Quando executar seu programa novamente,
essas palavras e dignificados novos devem ser incluídos automaticamente na saída.
"""

words = {'variável': 'palavra reservada que simboliza um valor na programação',
         'lista': 'lista de elementos',
         'if': 'estrutura de condição com testes lógicos',
         'dicionário': 'estrutura de dados de chave e valor',
         'objeto': 'estrutura de dados principal do python',
         'set': 'conjunto não ordenado',
         'string': 'lista de caracteres',
         'int': 'número inteiro',
         'f-string': 'string especial que concatena variáveis',
         'list comprehension': 'criação de lista com loops'
         }

for k, v in words.items():
    print(f"{k}: {v}")
