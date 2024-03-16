# 2. Napisati program koji nalazi ponavljajuću sekvencu (podniz) koja u proizvodu daje najveću
# vrijednost. Štampati tu sekvencu i proizvod te sekvence. Primjer: za listu [1, 2, 2, 2, 4, 4] treba da
# se štampa sekvenca [4, 4] i proizvod 16.

lista = input("Unesi clanove niza: ").split()
max = 0
for i in range(len(lista)):
    lista[i] = int(lista[i])

for i in range(len(lista) - 1):
    if (lista[i] * lista[i + 1]) > max:
        max = lista[i] * lista[i + 1]
        prvi = lista[i]
        drugi = lista[i + 1]
print(prvi, drugi, max)