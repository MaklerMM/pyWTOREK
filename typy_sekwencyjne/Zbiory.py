# # zbiory
#
# A = set([1,2,3,4,5,6])
# B = set([4,5,6,7,8])
#
# print("suma", A | B)
# print("czesc wspolna", A & B)
# print("roznica A i B", A - B)
# print("roznica B i A", B - A)
# print("roznica symetryczna", A ^ B)
#
# zdanie = input("podaj zdanie do analizy ").lower()
# zbior = set(zdanie.split())
# print(len(zbior), " ilosc slow")
# print(len(zdanie.split()) - len(zbior), " powtorzen")
#
#
from random import sample
population = range(1,50)
quantity = 6
los1 = sample(population, quantity)
print(los1)
los1.sort()
print(los1)
