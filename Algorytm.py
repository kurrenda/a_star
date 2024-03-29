from math import sqrt

class Obiekt():

    def __init__(self, rodzic, pozycja):
        self.rodzic = rodzic
        self.pozycja = pozycja

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.pozycja == other.pozycja


def agwiazdka(mapa):

    start = Obiekt(None, (0,19))
    start.g = 0
    start.h = 0
    start.f = 0

    koniec = Obiekt(None, (19,0))
    koniec.g = 0
    koniec.h = 0
    koniec.f = 0

    lista_otwarta = []

    lista_zamknieta = []

    lista_zamknieta.append(start)

    dlugosc_x_mapy = len(mapa)-1
    dlugosc_y_mapy = len(mapa[0])-1

    aktualna_pozycja = lista_zamknieta[len(lista_zamknieta) - 1].pozycja
    aktualna_pozycja_rodzic = lista_zamknieta[len(lista_zamknieta) - 1]

    gora = Obiekt(aktualna_pozycja, (aktualna_pozycja[0], aktualna_pozycja[1] + 1))
    dol = Obiekt(aktualna_pozycja, (aktualna_pozycja[0], aktualna_pozycja[1] - 1))
    lewo = Obiekt(aktualna_pozycja, (aktualna_pozycja[0] - 1, aktualna_pozycja[1]))
    prawo = Obiekt(aktualna_pozycja, (aktualna_pozycja[0] + 1, aktualna_pozycja[1]))

    pozycje_wokol_aktualnej = [gora, dol, lewo, prawo]

    for kierunek in pozycje_wokol_aktualnej:

        if 0 <= kierunek.pozycja[0] <= dlugosc_x_mapy and 0 <= kierunek.pozycja[1] <= dlugosc_y_mapy:

            kierunek.g = aktualna_pozycja_rodzic.g + 1
            kierunek.h = sqrt(((kierunek.pozycja[0] - koniec.pozycja[0]) ** 2 + (
                    kierunek.pozycja[1] - koniec.pozycja[1]) ** 2))
            kierunek.f = kierunek.g + kierunek.h
            kierunek.rodzic = aktualna_pozycja_rodzic

            lista_otwarta.append(kierunek)


    while len(lista_otwarta) > 0:

        wartosc_najmniejsza = lista_otwarta[0]
        index_wartosci_najmniejszej = 0

        for i in range(1, len(lista_otwarta)):
            if wartosc_najmniejsza.f >= lista_otwarta[i].f:
                wartosc_najmniejsza = lista_otwarta[i]
                index_wartosci_najmniejszej = i

        lista_zamknieta.append(wartosc_najmniejsza)
        lista_otwarta.pop(index_wartosci_najmniejszej)

        aktualna_pozycja = lista_zamknieta[len(lista_zamknieta)-1].pozycja
        aktualna_pozycja_rodzic = lista_zamknieta[len(lista_zamknieta) - 1]

        gora = Obiekt(aktualna_pozycja, (aktualna_pozycja[0], aktualna_pozycja[1] + 1))
        dol = Obiekt(aktualna_pozycja, (aktualna_pozycja[0], aktualna_pozycja[1] - 1))
        lewo = Obiekt(aktualna_pozycja,(aktualna_pozycja[0]-1, aktualna_pozycja[1]))
        prawo = Obiekt(aktualna_pozycja,(aktualna_pozycja[0]+1, aktualna_pozycja[1]))

        pozycje_wokol_aktualnej = [gora,dol,lewo,prawo]

        for kierunek in pozycje_wokol_aktualnej:

            if 0 <= kierunek.pozycja[0] <= dlugosc_x_mapy and 0 <= kierunek.pozycja[1] <= dlugosc_y_mapy:

                if mapa[kierunek.pozycja[0]][kierunek.pozycja[1]] == 5:
                    continue

                elif kierunek in lista_otwarta:
                    continue

                elif kierunek in lista_zamknieta:

                    kierunek.g = aktualna_pozycja_rodzic.g + 1
                    kierunek.h = sqrt(((kierunek.pozycja[0] - koniec.pozycja[0]) ** 2 + (
                                kierunek.pozycja[1] - koniec.pozycja[1]) ** 2))
                    kierunek.f = kierunek.g + kierunek.h
                    kierunek.rodzic = aktualna_pozycja_rodzic

                    for obiekt in lista_zamknieta:
                        if kierunek.pozycja == obiekt.pozycja:
                            if kierunek.f < obiekt.f:
                                obiekt.rodzic = kierunek.rodzic
                    continue

                else:
                    kierunek.g = aktualna_pozycja_rodzic.g + 1
                    kierunek.h = sqrt(((kierunek.pozycja[0] - koniec.pozycja[0]) ** 2 + (kierunek.pozycja[1] - koniec.pozycja[1]) ** 2))
                    kierunek.f = kierunek.g + kierunek.h
                    kierunek.rodzic = aktualna_pozycja_rodzic

                    lista_otwarta.append(kierunek)

        if wartosc_najmniejsza.pozycja == koniec.pozycja:
            print("Udało się dotrzeć do celu", "\n")


            sciezka = []

            krok = wartosc_najmniejsza

            sciezka.append(wartosc_najmniejsza.pozycja)

            while krok.pozycja != start.pozycja:
                krok = krok.rodzic
                sciezka.append(krok.pozycja)

            for i in sciezka:
                mapa[i[0]][i[1]] = 3

            for i in mapa:
                print(i)

            print(" ")

            sciezka.reverse()

            return sciezka

    else:

        print("Nie udało się dotrzeć do celu")
        print("\n")


def main():

    mapa = []

    with open('grid.txt', 'r') as f:
        x = f.read().splitlines()
        for i in x:
            mapa.append(i.split(" "))

    mapa_uporzadkowana = [[int(c) for c in line] for line in mapa]

    print(" ")
    print("Mapa wejściowa", "\n")

    for i in mapa_uporzadkowana:
        print(i)

    print(" ")
    print(agwiazdka(mapa_uporzadkowana))


if __name__ == '__main__':
    main()
