from math import sqrt


class Taczka():

    def __init__(self, rodzic, pozycja):
        self.rodzic = rodzic
        self.pozycja = pozycja

        self.g = 0
        self.h = 0
        self.f = 0



koniec1 = Taczka(None, (0,0))
koniec1.f = 2
koniec2 = Taczka(None, (0,0))
koniec2.f = 3
koniec3 = Taczka(None, (0,0))
koniec3.f = 1


lista_otwarta = [koniec1, koniec2, koniec3]
lista_zamknieta = []

wartosc_najmniejsza = lista_otwarta[0]
index_wartosci_najmniejszej = 0

for i in range(1, len(lista_otwarta)):
    if wartosc_najmniejsza.f >= lista_otwarta[i].f:
        wartosc_najmniejsza = lista_otwarta[i]
        index_wartosci_najmniejszej = i

lista_zamknieta.append(wartosc_najmniejsza)
lista_otwarta.pop(index_wartosci_najmniejszej)

for i in lista_zamknieta:
    print(str(i.f) + "zamk")

for i in lista_otwarta:
    print(i.f)





xd = sqrt(((1 - 19) ** 2 + (0 - koniec.pozycja[1] ** 2)))













