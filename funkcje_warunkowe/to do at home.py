# tabliczka mnozenia z formatowaniem
# # complex = range(1, 11)
# # for i in complex:
# #     for j in complex:
# #         print("%3x" % (i * j), end=" ")
# #     print()
# #
# # kw = range (3,10)
# # for i in kw:
# #         print("%3i ^ 2 = %i"
# #               % (i, i ** 2))

def celsiusToFarenheit(celsiusDegree):
    return 32 + (9 * celsiusDegree)/5

def temperatureTable (start, stop, step):
    print("| %5s | %6s |" % ("C", "F"))
    for celsiusDegree in range(stop, start - step, step):
        if (celsiusDegree == 0):
            print("| %5i | %6.1f | " % (celsiusDegree, celsiusToFarenheit(celsiusDegree)))
        else:
            print("| %+5i | %6.1f |" % (celsiusDegree, celsiusToFarenheit(celsiusDegree)))

# temperatureTable (-5,45,5)
temperatureTable(-5,45,5)
