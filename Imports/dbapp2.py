# import z okreslonej lokalizacji konkretnych skladowych
# skladowe sa dostepne bez adresowania

from Imports.SecretVariables import dataBase, username, password, Hello, getConnection
import random as rnd

# CTRL + ALT + O -> optimize import

print(username)
print(password)
print(dataBase)

# print(port) -> nie jest dostepny, bo nie zostal zaimportowany
print(getConnection())
h = Hello("MM")
print("\n")
# for i in dir(rnd):
#     print(i)

# help(rnd)

import os

print("Direct ref ", os.getcwd())
print(("W katalogu, w ktorym sie znajdujemy aktualnie: "))
for i in os.listdir('.'):
    print(i)

print(("W katalogu pracownikow jest cos takiego: "))
for i in os.listdir("C:\\Users\\user\\Desktop\\REAKTOR\\PYTHON\\firstPython\\programowanieObiektowe\\employee_mgm"):
    print(i)

os.chdir("C:\\Users\\user\\Desktop") # change directory
for file in os.listdir('.'):         # list directory w aktualnej lokalizacji
    print(file)

