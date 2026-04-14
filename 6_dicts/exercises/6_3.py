"""
6.3 Glossário:
Um dicionário Python pode ser usado para modelar um dicionário real.
Contudo, para evitar confusão, vamos chamá-lo de glossário.

- Pense em cinco palavras do mundo de programação que você aprendeu nos capítulos anteriores.
Use essas palavras como chaves em seu glossário e armazene seus significados como valores.
- Exiba cada palavra e seu significado como uma saída elegantemente formatada.
É possível até mesmo exibir a palavra seguida por dois-pontos e depois
seu significado ou a palavra em uma linha e, em seguida,
exibir seu significado indentado em uma segunda linha.
Use o caractere quebra de linha (\n) para inserir uma linha em branco
entre cada par palavra-significado em sua saída.
"""

words = {'variável': 'palavra reservada que simboliza um valor na programação',
         'lista': 'lista de elementos',
         'if': 'estrutura de condição com testes lógicos',
         'dicionário': 'estrutura de dados de chave e valor',
         'objeto': 'estrutura de dados principal do python'}

for k, v in words.items():
    print(f"{k}: {v}")
