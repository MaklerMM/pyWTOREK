# funkcja zwracajaca kolejna liczbe pierwsza wzgledem zadanej wartosci

# # def getPrimaryNumbers(n):
# # #     primaryNumbers() = [1]
# # #     isPrimary = False
# # #     while(len(primaryNumbers) <= n):
# # #         for l in range (2,1000):
# # #             for m in range (2,l):
# # #                 if (l % m == 0):
# # #                     primaryNumbers.append(l)
# # #         ilosc = len(primaryNumbers)
# # #     return primaryNumbers
#
#
# def getPrimaryNumbers(n = 100):
#     primaryNumbers = [1]
#     number = 2
#     while(len(primaryNumbers) < n):
#         isPrimary = True
#         for div in range(2,number):
#             if (number % div == 0): # sprawdzenie podzielnosci
#                 isPrimary = False
#         if(isPrimary):
#             primaryNumbers.append(number)
#         number += 1
#     return primaryNumbers, primaryNumbers[len(primaryNumbers) - 1]
#

from datetime import date

def printParameters(login, password, email, status=True, registrationDate=date.today()):
    return ("%s %s %s %s %s" % (login, password, email, status, registrationDate))

# wywolanie funkcji

print(printParameters("nk", "nk", "nk"))  #tylko argumenty obowiazkowe
print(printParameters("nk1", "nk1", "nk1", registrationDate='2020-01-01'))  #tylko argumenty obowiazkowe
print(printParameters("nk2", "nk2", "nk2", registrationDate='2020-01-01', status=False))  #tylko argumenty obowiazkowe
# element = 11
# print("Lista: ", getPrimaryNumbers(element)[0])
# print(element, "element: ", getPrimaryNumbers(element)[1])

def nonDefinedParameters(*elements): # parametr gwiazdka -> przyjmuje dowolna liczbe argumentow
    sum = 0
    for elem in elements:
        sum += elem
    return sum/len(elements)

print(nonDefinedParameters(1))
print(nonDefinedParameters(5,4,6))
print(nonDefinedParameters(2,4,3,12))

def sortList(numbers):
    numbers.sort()
    return numbers

list = [3,2,5,4,6]
print(sortList(list))
