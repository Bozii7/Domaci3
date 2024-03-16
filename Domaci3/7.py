class Book:
    def __init__(self, naslov, autor, godina_izdanja, broj_kopija):
        self.__naslov = naslov
        self.__autor = autor
        self.__godina_izdanja = godina_izdanja
        self.__broj_kopija = broj_kopija

    def get_naslov(self):
        return self.__naslov

    def set_naslov(self, naslov):
        self.__naslov = naslov

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        self.__autor = autor

    def get_godina_izdanja(self):
        return self.__godina_izdanja

    def set_godina_izdanja(self, godina_izdanja):
        self.__godina_izdanja = godina_izdanja

    def get_broj_kopija(self):
        return self.__broj_kopija

    def set_broj_kopija(self, broj_kopija):
        self.__broj_kopija = broj_kopija


class Library:
    def __init__(self):
        self.__inventar = []

    def dodaj_knjigu(self, knjiga):
        self.__inventar.append(knjiga)

    def obrisi_knjigu(self, naslov):
        for knjiga in self.__inventar:
            if knjiga.get_naslov() == naslov:
                self.__inventar.remove(knjiga)
                print("Knjiga '{}' je uspješno obrisana iz inventara.".format(naslov))
                return
        print("Knjiga '{}' nije pronađena u inventaru.".format(naslov))

    def pretrazi_po_naslovu(self, naslov):
        pronadjene_knjige = []
        for knjiga in self.__inventar:
            if naslov.lower() in knjiga.get_naslov().lower():
                pronadjene_knjige.append(knjiga)
        return pronadjene_knjige

    def pretrazi_po_autoru(self, autor):
        pronadjene_knjige = []
        for knjiga in self.__inventar:
            if autor.lower() in knjiga.get_autor().lower():
                pronadjene_knjige.append(knjiga)
        return pronadjene_knjige

    def prikazi_dostupne_knjige(self):
        print("Dostupne knjige:")
        for knjiga in self.__inventar:
            print("Naslov: {}, Autor: {}, Godina izdanja: {}, Broj kopija: {}".format(
                knjiga.get_naslov(), knjiga.get_autor(), knjiga.get_godina_izdanja(), knjiga.get_broj_kopija()))


biblioteka = Library()

while True:
    print("\n*** Dobrodošli u biblioteku ***")
    print("1. Dodaj knjigu")
    print("2. Pregled dostupnih knjiga")
    print("3. Pretraga po naslovu")
    print("4. Pretraga po autoru")
    print("5. Uredi knjigu")
    print("6. Obriši knjigu")
    print("7. Izlaz")
    izbor = input("Molimo unesite broj opcije: ")

    if izbor == '1':
        naslov = input("Unesite naslov knjige: ")
        autor = input("Unesite autora knjige: ")
        godina_izdanja = input("Unesite godinu izdanja knjige: ")
        broj_kopija = int(input("Unesite broj kopija knjige: "))
        nova_knjiga = Book(naslov, autor, godina_izdanja, broj_kopija)
        biblioteka.dodaj_knjigu(nova_knjiga)
        print("Knjiga uspješno dodana u inventar.")
    elif izbor == '2':
        biblioteka.prikazi_dostupne_knjige()
    elif izbor == '3':
        naslov_pretraga = input("Unesite naslov knjige za pretragu: ")
        pronadjene_knjige = biblioteka.pretrazi_po_naslovu(naslov_pretraga)
        if pronadjene_knjige:
            print("Pronađene knjige:")
            for knjiga in pronadjene_knjige:
                print("Naslov: {}, Autor: {}, Godina izdanja: {}, Broj kopija: {}".format(
                    knjiga.get_naslov(), knjiga.get_autor(), knjiga.get_godina_izdanja(), knjiga.get_broj_kopija()))
        else:
            print("Nema pronađenih knjiga sa zadatim naslovom.")
    elif izbor == '4':
        autor_pretraga = input("Unesite ime autora za pretragu: ")
        pronadjene_knjige = biblioteka.pretrazi_po_autoru(autor_pretraga)
        if pronadjene_knjige:
            print("Pronađene knjige:")
            for knjiga in pronadjene_knjige:
                print("Naslov: {}, Autor: {}, Godina izdanja: {}, Broj kopija: {}".format(
                    knjiga.get_naslov(), knjiga.get_autor(), knjiga.get_godina_izdanja(), knjiga.get_broj_kopija()))
        else:
            print("Nema pronađenih knjiga sa zadatim autorom.")
    elif izbor == '5':
        naslov_uredi = input("Unesite naslov knjige koju želite urediti: ")
        for knjiga in biblioteka.get_inventar():
            if knjiga.get_naslov() == naslov_uredi:
                print("Knjiga pronađena. Unesite nove podatke:")
                novi_naslov = input("Unesite novi naslov: ")
                novi_autor = input("Unesite novog autora: ")
                nova_godina_izdanja = input("Unesite novu godinu izdanja: ")
                novi_broj_kopija = int(input("Unesite novi broj kopija: "))
                knjiga.set_naslov(novi_naslov)
                knjiga.set_autor(novi_autor)
                knjiga.set_godina_izdanja(nova_godina_izdanja)
