globalId = 0
class Player:
    def __init__(self, name, lastname, club, weight, height):
        self.name = name
        self.lastname = lastname
        self.club = club
        self.weight = weight
        self.height = height
        global globalId     # modyfikacja wartosci globalnej w skrypcie
        globalId += 1       # global -> wskaznik globalny niezwiazany z klasa Player
        self.id = globalId  # self -> id dla konkretnego obiektu

    def calculateBMI(self):
        return self.weight / pow(self.height / 100, 2)

    def __str__(self):
        return ("| %3d | %10s | %15s | %10s | %8.2f |" % (self.id, self.name, self.lastname, self.club, self.calculateBMI()))

p1 = Player("Adam", "Małysz", "Wisła", 50, 165)
p2 = Player("Dariusz", " Pudzianowski", "Punisher", 130, 190)
p3 = Player("Robert", "Lewy", "Bayern", 76, 185)
p4 = Player("Zygmunt", "Hajser", "TVN", 96, 178)
p5 = Player("Władek", "Mors", "Mamry", 76, 171)


players = [p1, p2, p3, p4, p5]
for player in players:
    print(player)
