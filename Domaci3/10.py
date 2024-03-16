# 10. Potrebno je da kreirate klasu Color koja ima tri atributa: red, green i blue. Svaka boja ima
# vrijednosti između 0 i 255 (uključujući)
# ● Potrebno je kreirati konstruktor kojim se definišu vrijednosti sva tri atributa na zadate
# vrijednosti. Pretpostavlja se da korisnik unosi ispravno nformacije (ne treba raditi
# validaciju). Svi atributi su privatni.
# ● Potrebno je kreirati odgovarajuće getere i setere za sva tri atributa klase koji su
# definisani. Napomena: pri setovanju atributa potrebno je odraditi validaciju (moguće je
# unijeti cio broj između 0 i 255). Ako je unos nevalidan štampati odgovarajuću poruku
# ● Kreirati metod add_red koji sadrži osim parametra self, i parametar change koji označava
# za koliko treba izmijeniti vrijednost red atributa. Vrijednosti ovog parametra mogu da budu
# pozitivne ili negativne vrijednosti. Ako je u pitanju pozitivna vrijednost tada se uvećava
# vrijednost atributa red za zadatu vrijednost, a ako je negativna, onda se smanjuje.
# Obavezno provjeriti da li je došlo do ispadanja iz segmenta 0 i 255. (npr. ako je trenutno
# vrijednost za red = 20, a proslijedimo za change -40, to znači da je došlo do ispadanja iz
# segmenta 0 - 255, jer je 20 - 40 = -20 što je manje od 0).
# ● Potrebno je isto odraditi za green i blue atribute, tj. kreirati metode add_green i add_blue,
# oba metoda imaju osim parametra self i parametar change koji se obavlja izmjena
# odgovarajućih boja (u add_green ažurira se green atribut, a u add_blue ažurira se blue
# atribut)
# ● Potrebno je implementirati funkciju __lt__ gdje se definiše ponašanje operatora <.
# Funkcija treba da vrati True ako je color1 < color2. To je tačno ako su sve vrijednosti
# atributa (red, green i blue) color1 manje od svih vrijednosti atributa od color2. Potrebno je
# implementirati funkciju __eq__ koja vraća True ili False u zavisnosti od toga da li su dvije
# boje iste. Dvije boje su iste ako su sve vrijednosti tih atributa iste.
# ● Potrebno je implementirati funkciju __str__ koja vraća format stringa u kome se štampaju
# boju “red”: red_num, “green”: green_num, “blue”: blue_num

class Color:
    def __init__(self):
        self.red = 0
        self.blue = 0
        self.green = 0

    def get_red(self):
        return self.red

    def set_red(self, broj):
        if 0 <= broj <= 255:
            self.red = broj
        else:
            print("Lose unijeta vrijednost")

    def get_blue(self):
        return self.blue

    def set_blue(self, broj):
        if 0 <= broj <= 255:
            self.blue = broj
        else:
            print("Lose unijeta vrijednost")

    def get_green(self):
        return self.green

    def set_green(self, broj):
        if 0 <= broj <= 255:
            self.green = broj
        else:
            print("Lose unijeta vrijednost")

    def add_red(self, change):
        promjena = self.red - abs(change)
        if not 0 <= promjena <= 255:
            print("Ispali ste iz segmenta")

    def add_blue(self, change):
        promjena = self.blue - abs(change)
        if not 0 <= promjena <= 255:
            print("Ispali ste iz segmenta")

    def add_green(self, change):
        promjena = self.green - abs(change)
        if not 0 <= promjena <= 255:
            print("Ispali ste iz segmenta")

color1 = Color()
color1.set_red(100)
color1.set_blue(50)
color1.set_green(10)

color2 = Color()
color2.set_red(200)
color2.set_blue(150)
color2.set_green(100)

def ___it___(color3, color4):
    if color3.get_red() < color4.get_red() and color3.get_blue() < color4.get_blue() and color3.get_green() < color4.get_green():
        print(True)
    else:
        print(False)

___it___(color1, color2)

def ___eq___(color3, color4):
    if color3.get_red() == color4.get_red() or color3.get_blue() == color4.get_blue() or color3.get_green() == color4.get_green():
        print("Iste")
    else:
        print("Nisu iste")

___eq___(color1, color2)

def ___str___(color3):
    print(f'Crvena je {color3.get_red()}, plava je {color3.get_blue()} i zelena je {color3.get_green()}')

___str___(color1)



