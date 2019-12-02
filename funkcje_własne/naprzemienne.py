#funkcja odwolujaca sie do obiektu globalnego w skrypcie
def returnColor():
    global value # pobieram wartosc globalna
    value = not value
    return "black" if value else "white"

value = False
print(returnColor())
print(returnColor())
print(returnColor())
print(returnColor())
print(returnColor())
print(returnColor())
