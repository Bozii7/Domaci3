# 9. Napisati klasu Turnir koja se sastoji od sljedećih atributa: naziv_turnira (string), lista_igrača (lista
# torki oblika ime, broj_bodova), broj_rundi (integer). Potrebno je implementirati sljedeće
# funkcionalnosti:
# a. Konstruktor klase Turnir koji postavlja početne vrijednosti atributa naziv_turnira,
# lista_igrača, broj_igrača i broj_rundi. Atribut lista_igrača treba da bude prazna lista.
# b. Getteri i setteri za sve atribute klase. Obratiti pažnju na ograničenja atributa broj rundi čija
# vrijednost je veća od 0, a manja od 10.
# c. Funkciju dodaj_igrača sa parametrom ime_igrača koja dodaje novog igrača (torku) u listu
# igrača turnira tako da je broj_bodova inicijalno 0.
# d. Funkciju obriši_igrača sa parametrom ime_igrača kojom se briše igrač na osnovu
# unesenog imena.
# e. Funkciju prikazi_najboljeg_igrača koja prikazuje ime igrača koji je na putu da osvoji turnir.
# # To je igrač sa najvećim brojem bodova.

class Turnir:
    def __init__(self):
        self.naziv_turnira = ''
        self.lista_igraca = []
        self.broj_rundi = 0

    def get_naziv_turnira(self):
        return self.naziv_turnira
    def set_naziv_turnira(self, naziv):
        self.naziv_turnira = naziv

    def get_lista_igraca(self):
        return self.lista_igraca
    def set_lista_igraca(self, lista):
        self.lista_igraca = lista[:]

    def get_broj_rundi(self):
        return self.broj_rundi
    def set_broj_rundi(self, broj):
        if 0 < broj < 10:
            self.broj_rundi = broj

    def dodaj_igraca(self, ime):
        self.lista_igraca.append((ime, 0))

    def obrisi_igraca(self, ime):
        for i in range(len(self.lista_igraca)):
            if self.lista_igraca[i][0] == ime:
                self.lista_igraca[i] = 0
        self.lista_igraca.remove(0)

    def prikazi_najboljeg_igraca(self):
        i = 0
        maxi = -1
        for j in range(len(self.lista_igraca)):
            if self.lista_igraca[j][1] > maxi:
                i = j
        print(f'Najbolji igrac je: {self.lista_igraca[i][0]}')





