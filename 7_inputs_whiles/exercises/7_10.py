"""
7.10 Férias tão sonhadas:

Crie uma pesquisa que pergunte aos usuários sobre as férias de seus sonhos.
Crie um prompt mais ou menos assim: Se pudesse visitar qualquer lugar do mundo, para onde iria?
Inclua um bloco de código que exiba os resultados dessa pesquisa.
"""

poll_active = True
destinations = []

while poll_active:
    destination = input('Se pudesse visitar qualquer lugar do mundo, para onde iria?')
    destinations.append(destination)
    keep = input("Deseja continuar com a pesquisa? (s/n): ")
    if keep == "n":
        poll_active = False
print(f"Destinations: {", ".join(destinations)}")