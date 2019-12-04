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
for i in dir(rnd):
    print(i)

help(rnd)


