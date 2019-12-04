# importy sa adresowane od katalogu domowego -> nazwa projektu
# nazwa modulu wystepuje bez rozszerzenia
# alias zastepuje wszystko co jest w adresie modulu razem z jego nazwa

import Imports.SecretVariables as sv

print(sv.dataBase)
print(sv.username)
print(sv.password)
print(sv.host)
print(sv.port)

# dostep do metod
print(sv.getConnection())

# dostep do klas
obiektKlasyZaimportowanej = sv.Hello("Maciej")
print(obiektKlasyZaimportowanej.name)
print(obiektKlasyZaimportowanej)

