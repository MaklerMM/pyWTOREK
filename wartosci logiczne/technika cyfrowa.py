# pierwiastek z minusowej

# j2 = -1
# j = (-1)**(1/2)

SPK = float(input("podaj wartość początkową konta "))
roczna = float(input("podaj roczna stope w % "))/100
okresy = float(input("podaj liczbe okresow kapitalizacji w roku "))


koniec = SPK * (1 + (roczna/okresy))**(roczna*okresy)
print(koniec, " zl")