# produkty w slowniku
products = {"1": ["A", 3.5, 10],
            "2": ["B", 2.99, 5],
            "3": ["C", 9.99, 1],
            "4": ["D", 4.99, 25]
            }
# koszyk
basket = []
cumSum = 0

# GUI uzytkownika
while(True):
# petla wypisujaca produkty
    print(" |%2s |%5s |%12s |%6s |" % ("ID", "NAZWA", "CENA", "ILOść"))
    for key in products.keys():
        print(" |%2c |%5c |%9.2f zł |%6.1f |" % (key, products[key][0], products[key][1], products[key][2]))

    choice = input("W celu zamowienia produktu podaj jego id lub wpisz q aby zakończyć zamawianie ")

# wyjscie z programu
    if (choice.upper() == 'Q'):
        print("Twój koszyk: ")
        for goods in basket:
            print(" |%6s |%9.2f zł |%6.1f szt. " % (goods[0], goods[1], goods[2]))
        print("Suma do zapłaty ")
        print(" % 9.2f zł " % (cumSum))
        print("Dziękujemy i zapraszamy ponownie")
        break
# sprawdzenie czy istnieje taki id
    if (choice not in products.keys()):
        print("przykro nam, ale nie mamy takiego produktu")
        continue
# sprawdzenie dostępnych ilości produktu
    while (True):
        quantity = float(input("wprowadź ilość zamawianego produktu "))
        if (quantity > products[choice][2] and quantity >= 0):
            print("dostępna ilość ", products[choice][2])
            continue
        else:
            break
# aktualizacja magazynu i koszyka
    products[choice][2] -= quantity
    basket.append([products[choice][0], products[choice][1], quantity])
# suma skumulowana zamowien w koszyku
    cumSum += quantity * products[choice][1]
