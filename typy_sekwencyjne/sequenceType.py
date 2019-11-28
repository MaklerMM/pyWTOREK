# sentence = "Maja ma kota Zindi, a kot ma Panią Maje."
#
# # oczysc zdanie ze znakow interpunkcyjnych
#
# sentence = sentence.replace(",","")
# sentence = sentence.replace(".","")
# print(sentence)
#
# # zapisz wszystkie slowa osobno
#
# words = sentence.split(" ")
# print(words)
#
# # listy
# params = []
# row = [1, "Adam", "Nowak", "2000-01-01", True, 5500.]
#
# # dodawanie parametrow do params
# params.append(12.5)
# params.append(11.5)
# params.append(09.4)
# # wypisanie elementow listy
# print(params)
# print(row)
# # zmiana pensji
# row [5] = 6000.
# print(row)
# print(row[:0:-1])
# print(row[::-1])
#
# # powielanie listy
# row = row * 2
# print(row)
# # row *= 0 # czysci liste
# # zwraca dlugosc listy
# print(len(row))
# print("Nowak" in row)
# name = "Maciej"
# name = list(name)
# print(name)
# string = []
# for v in name:
#     string += v
#     print(string)
#
# # PALINDROM
#
# text = "kajak"
# print(text[::] == text[::-1])
#
# textList = list("kajak")
# textList.sort()
# print(textList)
#
# # listy wielowymiarowe
#
# kik = [
#         ["_","_","_"],
#         ["_","_","_","_"],
#         ["_","_","_","_","_"]
#         ]
# print(kik)
# print(len(kik[2]))
# kik[1][1:3] = ["O","O"]
# print(kik)
# kik.append(["*","*","*"])
# print(kik)
# # kik = [["l","l","l"]]+kik
# # print(kik)
#
# # dodawanie elementow do listy
# liczby = []
# liczby.append(input("Podaj liczbe "))
# liczby.append(input("Podaj liczbe "))
# liczby.append(input("Podaj liczbe "))
# imiona = []
# imiona.append(input("Podaj imie "))
# imiona.append(input("Podaj imie "))
# imiona.append(input("Podaj imie "))
# zestaw = [liczby] + [imiona]
# print(zestaw)

# convivience = ["chleb", "pasta", "woda", "pomidor", "maslo"]
# print(convivience[::len(convivience)-1])

dzien = 28
miesiac = 11
rok = 2019
data = (dzien, miesiac, rok)

print("Data ważności: ", data[1], " ", data[2])
