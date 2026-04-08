name = "Vinícius Cavalcante"
message = f"Olá, {name}, gostaria de aprender um pouco Python hoje?"
print(message)

name_upper = name.upper()
name_lower = name.lower()
name_title = name.title()

print(name_upper)
print(name_lower)
print(name_title)

author = "Albert Einstein"
citation = "Uma pessoa que nunca cometeu um erro nunca tentou nada de novo"

message_citation = f"{author} disse uma vez: \"{citation}\"."
print(message_citation)

wrong_typed_name = " \tViní\ncius "
print(wrong_typed_name)
print(wrong_typed_name.lstrip())
print(wrong_typed_name.rstrip())
print(wrong_typed_name.strip())

filename = "pythonnotes.txt"
print(filename.removesuffix(".txt"))