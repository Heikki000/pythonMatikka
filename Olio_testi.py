#testaamista

class Juoksu:
    def __init__(self, nimi, nopeus, lopputulos):
        self.nimi = nimi
        self.nopeus = nopeus
        self.lopputulos = lopputulos
        self.matka = 0

    def juokse(self, meters):
        if self.matka < 100:
            self.matka += int(meters)
        else:
            print("Olet jo maalissa")
            return False

juoksija_1 = Juoksu("Zune", 10, 0)
while True:
    matka = input("Kuinka paljon juostaan:")
    juoksija_1.juokse(matka)
    if juoksija_1.matka > 100:
        break

print(juoksija_1.matka)

