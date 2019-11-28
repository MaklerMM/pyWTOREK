# # slowniki
#
# products = {}
# #dodanie nowego produktu
# products[1] = "I"
# products[2] = "II"
# products[3] = "III"
# products[4] = "IV"
# products[5] = "V"
# products[6] = "VI"
# products[7] = "VII"
# products[8] = "VIII"
# products[9] = "IX"
#
# # modyfikacja pamieci RAM
# podana = input("podaj liczbe 1 - 9 ")
# if (podana.isdecimal()):
#     podana = int(podana)
#     if (podana < 10 and podana in products):
#         print(products[podana], podana)
#     else:
#         print("Podales bledne dane ")
# else:
#     print("Podales bledne dane ")
#
# print((products))

# products = {nazwa : [ilosc, cena_netto, cena_brutto]}
koniec = ''
products ={}
while(koniec != 'k'):
    nazwa = input("podaj nazwe towaru ")
    ilosc = input("podaj ilosc towaru ")
    cena_netto = input("podaj cene netto towaru ")
    cena_brutto = input("podaj cene brutto towaru ")
    koniec = input("konczymy? wprowadz k ").lower()
    products[nazwa] = [ilosc, cena_netto, cena_brutto]
print(products)

