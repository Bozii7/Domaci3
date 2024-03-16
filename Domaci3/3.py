# 3. Napisati Python funkciju kojom tražite najduži testerasti podniz. Testerasti podniz je onaj za koji
# važi da je prvi broj manji od drugog, drugi da je veći od trećeg, treći manji od četvrtog, itd.

def testerasti(niz):
    ind = 0
    for i in range(len(niz) - 1):
        if i % 2 == 0:
            if niz[i] > niz[i + 1]:
                ind = 1
    if ind == 0:
        print("Niz je testerast.")
    elif ind == 1:
        print("Niz nije testerast.")


niz = [3, 1, 2, 4, 3]
testerasti(niz)

