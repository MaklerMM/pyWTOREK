# CTRL + / -> komentarz
'''
komentarz
blokowy
'''

print("Witaj na kursie Pythona")
# zmienne -> deklaracja i przypisanie -> inicjalizacja zmiennej (obiektu)
text = "dzien dobry"
name = "Macieju"
sign = 'a'
print(text + " " + name)

# zmienne na podstawie innych zmiennych
a = 1
b = a + 1
print(a,b, a + b)
print(a, end=';')
print(b,end=';')
print(a + b, end='\n')  # \n - new line
print('www.xyz.pl\\all') # \\ - '\'
print('"Cytat"')  # opakowanie w ' apostrofy
print("\"Cytat\"") # lub opakowujemy w backslash'e

# usuwanie obiektu z pamieci
a = 2
print(a)
del(a)
# print(a) -> a is not defined

a = 1
b = 2.4
c = "w1"

print(a,b,c, sep=' | ')

a = 2.1
b = "abc"
c = 0

print(a,b,c, sep=' | ')

a = 13
b = c
print(a,b,c, sep=' | ')

del(a)
del(c)
# print(c + 31.3)
# c = c + 31.3 -> c is not defined

