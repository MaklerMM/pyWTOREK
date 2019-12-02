# from datetime import date
#
#
# class Auto:
#     # pola klasowe -> obiekty, zmienne
#     brand = "b/d"
#     model = "b/d"
#     # metody klasowe -> funkcje
#
#     def helloInClass(self):
#         return "Witaj w programowaniu obiektowym"
#
# # utworzenie obiektu
# a = Auto()
# print(a.helloInClass())
# print(a.brand)
# a.brand = "BMW"
# a.model = "X3"
# print(a.brand, a.model)
#
# class User:
#     def __init__(self, login, password, status, registrationDate): # metoda wywolywana jako pierwsza przy tworzeniu obiektu
#         # pole klasowe
#         self.login = login
#         self.password = password
#         self.status = status
#         self.registrationDate = registrationDate
#     def setStatus(self, status):
#         self.status = status
#
# # funkcje specjalne
# def __str__(self):  # funkcja wywolywana gdy obiekt jest rzutowany do napisu
#     return ("| %10s | %10s | %8s | %10s |" % (self.login, self.password, self.status, self.registration))
#
#
# u1 = User("mm@wp.pl","12345", True, date.today())
# print(u1.login, u1.password, u1.status, u1.registrationDate)
# print(u1)
# u1.setStatus(False)
# u2 = User("gg@gg.pl", "97531", True, date.today())
# u3 = u2
# u2.status = True
# print(u2.status, u3.status)
# print(u1, u2, u3)
# print(u1)

# Napisz program OOP, ktory reprezentuje skladowe barw RGB
# R
# G
# B
# implementacja klasy reprezentujacej dowolny kolor
class RGB:
    def __init__(self, r, g, b):
        if(r >= 0 and g >= 0 and b >= 0 and r <= 255 and g <= 255 and b <= 255):
            self.r = r
            self.g = g
            self.b = b
        else:
            print("Podane wartości nie są poprawne")
            self = None
    def __add__(self, other):
        # utworzenie nowego obiektu na podstawie sumy skladowych r g b z dwoch kolorow
        c = RGB(self.r + other.r, self.g + other.g, self.b + other.b)
        return c
    def __eq__(self, other):
        return self.r == other.r, self.g == other.g, self.b == other.b
    def __str__(self):
        return("[%d, %d, %d]" % (self.r, self.g, self.b))

red = RGB (255,0,0)
green = RGB (0,255,0)
yellow = RGB (255,255,0)

print(red, green, yellow)
print("Czy zolty to to samo co czerwony plus zielony: ", "tak" if (yellow == (red + green)) else "nie")