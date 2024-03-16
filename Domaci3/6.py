# 6. Napisati klasu Televizor koja se sastoji od sledećih atributa: broj tekućeg kanala (int, između 0 i
# dužine od liste kanala), naziv tekućeg kanala (string), kanali (lista stringova), jačina tona (int,
# između 0 i 10). Potrebno je odraditi sledeće:
# a. Napisati konstruktor kojim se postavljaju početne vrijednosti atributa. Za atribut kanali to
# treba da bude prazna lista.
# b. Kreirati odgovarajući getere i setere. Obratiti pažnju na ograničenja za attribute broj
# kanala i jačina tona.
# c. Napisati funkciju dodaj_kanal sa parametrom naziv kanala, koja dodaje novi kanal u listu
# kanala.
# d. Napisati funkciju obriši_kanal sa parametrom na naziv kanala, kojom se briše kanal na
# osnovu naziv.
# e. Napisati funkciju pojačaj_ton koja uvećava vrijednost tona za jedan u odnosu na
# trenutnu jačinu
# f. Napisati funkciju ime_kanala sa parametrom za broj kanala, koja vraća naziv kanala na
# osnosu zadatog broja.Prvi kanal se nalazi na poziciji 1.

class Televizor:
    def __init__(self):
        self.broj_tekuceg_kanala = 1
        self.naziv_tekuceg_kanala = ""
        self.kanali = []
        self.jacina_tona = 5

    def get_broj_tekuceg_kanala(self):
        return self.broj_tekuceg_kanala

    def set_broj_tekuceg_kanala(self, broj):
        if 0 <= broj < len(self.kanali):
            self.broj_tekuceg_kanala = broj
            self.naziv_tekuceg_kanala = self.kanali[broj]
        else:
            print("Navedeni broj kanala nije validan.")

    def get_naziv_tekuceg_kanala(self):
        return self.naziv_tekuceg_kanala

    def get_kanali(self):
        return self.kanali

    def dodaj_kanal(self, naziv_kanala):
        self.kanali.append(naziv_kanala)

    def obrisi_kanal(self, naziv_kanala):
        if naziv_kanala in self.kanali:
            self.kanali.remove(naziv_kanala)
        else:
            print("Nema tog kanala")

    def pojacaj_ton(self):
        if self.jacina_tona < 10:
            self.jacina_tona += 1

    def ime_kanala(self, broj_kanala):
        if 1 <= broj_kanala <= len(self.kanali):
            return self.kanali[broj_kanala - 1]
        else:
            return "Ne postoji ovaj kanal."

tv = Televizor()
tv.dodaj_kanal("CNN")
tv.dodaj_kanal("BBC")
tv.dodaj_kanal("Discovery")
print("Kanali:", tv.get_kanali())

tv.obrisi_kanal("BBC")
print("Kanali nakon brisanja:", tv.get_kanali())

tv.set_broj_tekuceg_kanala(0)
print("Trenutni kanal:", tv.get_naziv_tekuceg_kanala())

tv.pojacaj_ton()
print("Jačina tona:", tv.jacina_tona)