name = input("Podaj imię: ")
salaryNet = float(input("Wprowadz cene brutto "))

print(name, "Cena brutto ", round(salaryNet,2), "\nCena netto z 3% podatkiem", round(salaryNet/1.03, 2), "\nCena netto z 7% podatkiem", round(salaryNet/1.07, 2), "\nCena netto z 23% podatkiem", round(salaryNet/1.23, 2))
#
# print(type(lastName))
# print(type(salaryNet))
# print(type(isActivated))