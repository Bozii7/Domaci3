# 8. Potrebno je kreirati klasu Player koja ima 5 atributa: x (x koordinata, integer), y (y koordinata,
# integer), width (širina, integer), height (visina, integer), health (životni bodovi, integer)
# a. Potrebno je kreirati konstruktor kojim se definišu vrijednosti svih atributa na zadate
# vrijednosti. Pretpostavlja se da korisnik unosi ispravno informacije (ne treba raditi
# validaciju). Svi atributi su privatni.
# b. Potrebno je kreirati odgovarajuće getere i setere za sve atribute Pri postavljanju
# vrijednosti atributa health onemogućiti postavljanje na vrijednosti koje su manje od 0, a
# veće od 100.
# c. Potrebno je kreirati klasu Enemy koja ima takođe 5 atributa: x, y, width, height i damage
# (vrijednost napada, integer)
# i. Potrebno je kreirati konstruktor kojim se definišu vrijednosti svih atributa na
# zadate vrijednosti. Pretpostavlja se da korisnik unosi ispravno informacije (ne
# treba raditi validaciju). Svi atributi su privatni.
# ii. Potrebno je kreirati odgovarajuće getere i setere za sve atribute Pri postavljanju
# vrijednosti atributa damage onemogućiti postavljanje na vrijednosti koje su manje
# od 0, a veće od 100.
# d. Potrebno je napraviti funkciju check_collision(player, enemy) koja provjerava da li se
# objekti player i enemy sudaraju.
# e. Potrebno je kreirati metod decreate_health(player, enemy) tako da se trenutna
# vrijednost atributa health objekta player smanjuje za vrijednost atributa damage objekta
# enemy ako se desi detekcija kolozije između player i enemy.
# f. Kreirati bar jedan objekat player i dva objekta tipa enemy

class Player:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__width = 0
        self.__height = 0
        self.__health = 0

    def get_x(self):
        return self.__x
    def set_x(self, broj):
        self.__x = broj

    def get_y(self):
        return self.__y
    def set_y(self, broj):
        self.__y = broj

    def get_width(self):
        return self.__width
    def set_width(self, broj):
        self.__width = broj

    def get_height(self):
        return self.__height
    def set_height(self, broj):
        self.__height = broj

    def get_health(self):
        return self.__health
    def set_health(self, broj):
        if 0 <= broj <= 100:
            self.__health = broj


class Enemy:
    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__width = 0
        self.__height = 0
        self.__damage = 0

    def get_x(self):
        return self.__x

    def set_x(self, broj):
        self.__x = broj

    def get_y(self):
        return self.__y

    def set_y(self, broj):
        self.__y = broj

    def get_width(self):
        return self.__width

    def set_width(self, broj):
        self.__width = broj

    def get_height(self):
        return self.__height

    def set_height(self, broj):
        self.__height = broj

    def get_damage(self):
        return self.__damage

    def set_damage(self, broj):
        if 0 <= broj <= 100:
            self.__damage = broj


player1 = Player()
player1.set_x(5)
player1.set_y(5)
player1.set_width(10)
player1.set_height(15)
player1.set_health(100)

enemy2 = Enemy()
enemy2.set_x(6)
enemy2.set_y(7)
enemy2.set_width(5)
enemy2.set_height(10)
enemy2.set_damage(10)

def check_collision(player, enemy):
    if player.get_x() == enemy.get_x() and player.get_y() == enemy.get_y():
        print("Desila se kolizija!")
    else:
        print("Nije se desila kolizija")

check_collision(player1, enemy2)

def decrease_health(player, enemy):
    remaining_health = player.get_health() - enemy.get_damage()
    print(remaining_health)


decrease_health(player1, enemy2)

