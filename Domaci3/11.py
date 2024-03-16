# 11. (Nastavak prethodnog zadatka). Potrebno je da kreirate klasu AlphaColor koja je izvedena iz
# klase Color (nasleđuje sve iz klase Color), a ima još jedan dodatni atribut alpha.
# ● Potrebno je kreirati konstruktor koji poziva konstruktor iz osnovne klase (koristiti super()
# specijalni metod) koji setuje red, green i blue u klasi Color, a nakon poziva super() u
# konstruktoru setovati vrijednost privatnog atributa alpha.
# ● Potrebno je kreirati geter i seter za alpha atribut. Alpha atribut može da ima vrijednosti
# između 0 i 1 (float vrijednosti)
# ● Potrebno je kreirati metod update_color_by_alpha koji osim self parametra sadrži i
# parametar alpha. Parametrom alpha se mijenja svaka boja tako što se od trenutne
# vrijednosti boje oduzme trenutna vrijednost boje pomnožena sa parametrom alpha (ako
# je boja imala vrijednost 200, a alpha je 0.5, nova vrijednost boje je 200 - 200*0.5 = 100).
# Iskoristiti setere i getere iz klase Color.
# ● Potrebno je implementirati funkciju __str__ koja vraća format stringa u kome se štampaju
# boju “red”: red_num, “green”: green_num, “blue”: blue_num, “alpha”:alpha_num
# ● Potrebno je kreirati bar dvije instance klase AlphaColor i testirati sve metode koje ste
# implementirali
#
