# baza danych
productsNames = "Chleb", "Mleko", "Cukierki"
productsPrices = 1.99, 2.50, 12.99
productsQuantity = "szt.", "l", "kg"

# zamowienie
productsOrder = 2, 0.5, 0.3

# prezentacja zamowienia
print(productsNames[0], productsOrder[0], productsQuantity[0], sep='\t\t')
print(productsNames[1], productsOrder[1], productsQuantity[1], sep='\t\t')
print(productsNames[2], productsOrder[2], productsQuantity[2], sep='\t\t')

# kwota do zaplaty

print("SUMA", round(productsPrices[0] * productsOrder[0] + productsPrices[1] * productsOrder[1] + productsPrices[2] * productsOrder[2], 2), " zl")
print("")
print((2+5j)*(4+6j))
print(4-(4+6j))


