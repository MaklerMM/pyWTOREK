from datetime import datetime


def bubbleSort(elements, asc=True):
    noProbes = 1
    for probe in range(len(elements)-1): #determinujemy 5 prob w najgorszym przypadku
        isSorted = True
        for index, value in enumerate(elements):
            if (index == len(elements) - 1):
                break
            if (elements[index] > elements[index + 1] and asc):
                isSorted = False
                elem = elements[index + 1]
                elements[index + 1] = elements[index]
                elements[index] = elem
            if (elements[index] < elements[index + 1] and not asc):
                isSorted = False
                elem = elements[index + 1]
                elements[index + 1] = elements[index]
                elements[index] = elem
#        print(noProbes, elements)
        if (isSorted): # sprawdzenie czy bylismy w ifie zwiazanym z sortowaniem danych
            break
        noProbes += 1
    return elements

print(bubbleSort([3,2,5,6,1,4,21,32,12,11,42,7,9,15]))
t_start = datetime.now().microsecond
print(bubbleSort([3,2,5,6,1,4,21,32,12,11,42,7,9,15], asc=False))
t_stop = datetime.now().microsecond
print(t_start)
print(t_stop)

