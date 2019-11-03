from math import sqrt

class Obiekt():

    def __init__(self, rodzic, pozycja):
        self.rodzic = rodzic
        self.pozycja = pozycja

        self.g = 0
        self.h = 0
        self.f = 0


def agwiazdka(mapa):


    start = Obiekt(None, (0,0))
    start.g = 0
    start.h = 0
    start.f = 0

    koniec = Obiekt(None, (9,9))
    koniec.g = 0
    koniec.h = 0
    koniec.f = None

    lista_otwarta = []

    lista_zamknieta = []

    lista_zamknieta.append(start)
    lista_otwarta.append(start)

    dlugosc_x_mapy = len(mapa)-1
    dlugosc_y_mapy = len(mapa[0])-1

    print(dlugosc_x_mapy,dlugosc_y_mapy)

    while len(lista_otwarta) > 0:

        aktualna_pozycja = lista_zamknieta[len(lista_zamknieta)-1].pozycja

        lewo = Obiekt(aktualna_pozycja,(aktualna_pozycja[0]-1, aktualna_pozycja[1]))
        prawo = Obiekt(aktualna_pozycja,(aktualna_pozycja[0]+1, aktualna_pozycja[1]))
        gora = Obiekt(aktualna_pozycja,(aktualna_pozycja[0], aktualna_pozycja[1]+1))
        dol = Obiekt(aktualna_pozycja,(aktualna_pozycja[0], aktualna_pozycja[1]-1))

        pozycje_wokol_aktualnej = [lewo,prawo,gora,dol]

        for kierunek in pozycje_wokol_aktualnej:

            if 0 <= kierunek.pozycja[0] <= dlugosc_x_mapy and 0 <= kierunek.pozycja[1] <= dlugosc_y_mapy:

                print(kierunek.pozycja[0], kierunek.pozycja[1], mapa[kierunek.pozycja[0]][kierunek.pozycja[1]])
                if mapa[kierunek.pozycja[0]][kierunek.pozycja[1]] == 5:
                    continue

                kierunek.g = kierunek.g + 1
                kierunek.h = sqrt(((kierunek.pozycja[0] - koniec.pozycja[0]) ** 2 + (kierunek.pozycja[1] - koniec.pozycja[1]) ** 2))
                kierunek.f = kierunek.g + kierunek.h

                for obiekt in lista_zamknieta:
                    if kierunek.pozycja == obiekt.pozycja:
                        if kierunek.f < obiekt.f:
                            obiekt.rodzic = kierunek.rodzic

                lista_otwarta.append(kierunek)

        wartosc_najmniejsza = lista_otwarta[0]
        index_wartosci_najmniejszej = 0

        for i in range(1, len(lista_otwarta)):
            if wartosc_najmniejsza.f >= lista_otwarta[i].f:
                wartosc_najmniejsza = lista_otwarta[i]
                index_wartosci_najmniejszej = i

        lista_zamknieta.append(wartosc_najmniejsza)
        lista_otwarta.pop(index_wartosci_najmniejszej)

        if wartosc_najmniejsza.pozycja == koniec.pozycja:
            print("Udało się dotrzeć do celu")
            break

    else:
        print("Nie udało się dotrzeć do celu")


    for i in lista_zamknieta:
        print(i.pozycja, end='')

def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    print(maze[0][4])

    agwiazdka(maze)


if __name__ == '__main__':
    main()
