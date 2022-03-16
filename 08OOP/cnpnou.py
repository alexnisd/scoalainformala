class Cnp:

    variante = 13

    def __init__(self, lungime):
        self.lungime = lungime
        if self.lungime != 13:
            print("lungime incorecta")


verificare = Cnp(input("Introdu cnp: "))
