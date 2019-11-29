# dana jest lista wartosci
# a = [.3, .4, 3.2, .5, 1, 5.4, 2, 1.1, 5, 7, 3.4, 5.1, 4.3, 1.2, 2.4, 9.1, 3.1, 5.6, 1.2, 1.7, 3.4, 8.1, 9.1, 10.4]
# below = []
# between =[]
# above =[]
# labelsDict = {0: below, 1: between, 2: above}
# treshold1 = float(input('podaj pierwsza wartosc progu odciecia '))
# treshold2 = float(input('podaj druga wartosc progu odciecia '))
#
# if (treshold1 > treshold2):
#     for w in a:
#         if (w >= treshold1):
#             above.append(w)
#         elif (w >= treshold2 and w < treshold1):
#             between.append(w)
#         else:
#             below.append(w)
# else:
#     for w in a:
#         if (w >= treshold2):
#             above.append(w)
#         elif (w < treshold2 and w >= treshold1):
#             between.append(w)
#         else:
#             below.append(w)
#
# print(" ponizej ", treshold1 if (treshold2 > treshold1) else treshold2, below)
# print(" pomiedzy ", str(treshold1) + " a " + str(treshold2) if (treshold2 > treshold1) else str(treshold2) + " a " + str(treshold1), between)
# print(" powyzej ", treshold1 if (treshold1 > treshold2) else treshold2, above)

##############################################
lvls = [ "A1", "A2", "B1", "B2", "C1", "C2" ]

for index, lvl in enumerate(lvls):
    print(index, lvl)

##############################################
lvlsNames = {lvls[0] : "basic",
             lvls[1] : "basic",
             lvls[2] : "independent",
             lvls[3] : "independent",
             lvls[4] : "proficient",
             lvls[5] : "proficient"
             }

for key in lvlsNames.keys():
    print(key, lvlsNames[key])