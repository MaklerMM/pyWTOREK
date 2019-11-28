# # system logowania
#
# users = {"admin": "a123", "user": "u123"}
#
# login: str = input("podaj login ")
# haslo = input("podaj haslo ")
#
# print ("bledny login lub haslo")\
#     if (login not in users.keys())\
#     else print ("bledny login lub haslo")\
#     if (haslo != users[login])\
#     else print("zalogowany")

znak = ''
lista = []
while (znak != 'q'):
    lista.append(znak)
    znak = input("wprowadz znak ").lower()

print(lista)