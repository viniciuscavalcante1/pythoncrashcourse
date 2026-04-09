"""
Exercício 1 — Gerador de crachá
Crie variáveis para nome, sobrenome e cargo de uma pessoa. Printe um crachá formatado assim:
========================
   ADA LOVELACE
   Cargo: Engenheira
========================
"""

first_name = "Ada"
last_name = "Lovelace"
role = "Engenheira"

full_name_upper = f"{first_name.upper()} {last_name.upper()}"
role_title = role.title()
number_sep = 25
sep = "=" * number_sep

print(sep)
print(f"\t{full_name_upper}")
print(f"\tCargo: {role_title}")
print(sep)

"""
Exercício 2 — Limpador de input
Simule dados sujos de usuário:
pythonusername = "   Ada_Lovelace   "
email = "   ADA@email.COM  "
Limpe e padronize os dados, e printe uma confirmação de cadastro com os valores corrigidos.
"""

username = "   Ada_Lovelace   "
email = "   ADA@email.COM  "
username = username.lower().strip()
email = email.lower().strip()
print(f"Usuário: {username}, email: {email}")

"""
Exercício 3 — Calculadora de corrida
pythondistance_km = 5.0
time_minutes = 32.5
A partir dessas variáveis, calcule pace (min/km) e velocidade (km/h). Printe tudo formatado.
"""

distance_km = 5.0
time_minutes = 32.5

pace = time_minutes / distance_km
velocity = distance_km / (time_minutes / 60)
print(f"Your pace is {pace:.1f}, with {velocity:.1f} km/h")

"""
Exercício 4 — Formatador de URL
pythonurl = "   HTTPS://WWW.Github.Com/meu-projeto   "
Transforme isso em www.github.com/meu-projeto. Printe cada etapa da transformação.
"""

url = "   HTTPS://WWW.Github.Com/meu-projeto   "

print(url)
url = url.lower()
print(url)
url = url.strip()
print(url)
url = url.removeprefix("https://")
print(url)

"""
Exercício 5 — Recibo simples
Crie variáveis para três produtos com nome e preço. Printe um recibo formatado com tabulações, quebras de linha e o total calculado.
"""

banana, price_banana = "banana", 10
uva, price_uva = "uva", 20
melon, price_melon = "melão", 10

print(sep)
print(banana, price_banana)
print(uva, price_uva)
print(melon, price_melon)
print(sep)
print(f"total \t {price_banana + price_uva + price_melon}")

"""
Exercício 6 — Debug intencional
O código abaixo tem 4 erros. Corrija um por vez, lendo o traceback a cada tentativa:
pythongreeting = "Olá"
Name = "vini
message = f"{greeting}, {name}! Bem-vindo ao Python."
print(mesage)
Depois de corrigir, adicione um comentário acima de cada linha.
"""

# greeting string
greeting = "Olá"
# name string
name = "vini"
# message variable with concatenation of greeting, name and a follow message
message = f"{greeting}, {name}! Bem-vindo ao Python."
# print message
print(message)

"""
Exercício 7 — Constantes e conversão
Defina constantes para taxas de câmbio USD→BRL e EUR→BRL. Crie um salário em USD usando underscore nos dígitos. Converta e printe os três valores formatados.
"""

USD_BRL = 5.15
EUR_BRL = 6.02

usd_sallary = 8_000
print(f"USD salary {usd_sallary}, BRL salary {usd_sallary * USD_BRL}, EUR salary {(usd_sallary * USD_BRL) / EUR_BRL}")