current_number = 1
while current_number <= 5:
    if current_number == 4:
        current_number += 1
        continue
    print(current_number)
    current_number += 1

active = True
while active:
    message = input("Me diga qualquer coisa e repetirei (q pra sair): ")
    if message == "q":
        active = False
    else:
        print(message)

while True:
    message = input("Me diga qualquer coisa e repetirei (q pra sair): ")
    if message == "q":
        break
    else:
        print(message)

