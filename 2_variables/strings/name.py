name = "vinicius cavalcante"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "Vinicius"
last_name = "Cavalcante"
full_name = f"{first_name} {last_name}"
print(full_name)

tab = "\t"
breakline = "\n"

print(f"{tab} tab {breakline} breakline")

favorite_language = "python "
favorite_language = favorite_language.rstrip()
favorite_language = "python "
favorite_language = favorite_language.lstrip()
favorite_language = " python "
favorite_language = favorite_language.strip()

url = "www.google.com"
url = url.removeprefix("www.")
url = url.removesuffix(".com")
print(url)