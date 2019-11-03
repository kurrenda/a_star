from itertools import product

class Obiekt():

    def __init__(self, rodzic, pozycja):
        self.rodzic = rodzic
        self.pozycja = pozycja

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.pozycja == other.pozycja



koniec1 = Obiekt(None, (1,9))
koniec2 = Obiekt(None, (9,9))
koniec3 = Obiekt(None, (1,9))
koniec4 = Obiekt(None, (9,9))


koniec5 = Obiekt(None, (0,9))

lista_otwarta = [koniec1,koniec2,koniec3,koniec4]

tablica = [koniec5,koniec4]


for i in range(4):
    for x in tablica:
        if x not in lista_otwarta:
            lista_otwarta.append(x)
            continue
    print(i)

for i in lista_otwarta:
    print(i.pozycja)