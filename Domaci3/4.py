# 4. Za zadati string napisati program kojim se provjerava koliko puta se u stringu dva susjedna
# karaktera ponavljaju (poklapaju).
# Primjer: aabaaac rezultat je 3.

s = input("Unesi string: ")
br = 0
max = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        br += 1
    if br > max:
        max = br
print(max)