# CTRL + ALT +L -> auto-formating
class Warcaby:
    # CTRL + f
    # pole klasowe -> slownik zawierajacy 8 slownikow

    warcaby = {
            8:{1:"-", 2:"O", 3:"-", 4:"O", 5:"-", 6:"O", 7:"-", 8:"O"},
            7:{1:"O", 2:"-", 3:"O", 4:"-", 5:"O", 6:"-", 7:"O", 8:"-"},
            6:{1:"-", 2:"O", 3:"-", 4:"O", 5:"-", 6:"O", 7:"-", 8:"O"},
            5:{1:"-", 2:"-", 3:"-", 4:"-", 5:"-", 6:"-", 7:"-", 8:"-"},
            4:{1:"-", 2:"-", 3:"-", 4:"-", 5:"-", 6:"-", 7:"-", 8:"-"},
            3:{1:"X", 2:"-", 3:"X", 4:"-", 5:"X", 6:"-", 7:"X", 8:"-"},
            2:{1:"-", 2:"X", 3:"-", 4:"X", 5:"-", 6:"X", 7:"-", 8:"X"},
            1:{1:"X", 2:"-", 3:"X", 4:"-", 5:"X", 6:"-", 7:"X", 8:"-"}
}

# metoda klasowa wypisujaca szachownice
    def printBoard(self):
        print("  |   %1s  |   %1s  |   %1s  |   %1s  |   %1s  |   %1s  |   %1s  |   %1s  |" % ("A", "B", "C", "D", "E", "F", "G", "H"))
        for row in self.warcaby.keys():
            print("%1d " % (row), end="")
            for key in self.warcaby[row].keys():
                print("| %3s " % (self.warcaby[row][key]), end=" ")
            print("|\n", end="")
        print("  |   %1s  |   %1s  |   %1s  |   %1s  |   %1s  |   %1s  |   %1s  |   %1s  |" % ("A", "B", "C", "D", "E", "F", "G", "H"))

    def checkMoveFromTo(self, rowStart, columnStart, rowStop, columnStop, type):
    # sprawdzam czy punkty znajduja sie w kluczach naszych slownikow
        if (rowStart in self.warcaby.keys() and columnStart in self.warcaby[rowStart].keys()):
    # sprawdzenie poprawnosci ruchu
            if (type == 'X' and rowStop == rowStart + 1):
                print("poprawny")

    def movePoint (self, rowStart, columnStart, rowStop, columnStop, type):
        # przesuniecie pionka na nowa pozycje
        self.warcaby[rowStop][columnStop] = type
        # aktualizacja pustego miejsca pozostalego po pionku
        self.warcaby[rowStart][columnStart] = "-"
        self.printBoard()




w = Warcaby()
w.printBoard()
