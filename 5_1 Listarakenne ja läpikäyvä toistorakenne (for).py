#Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
#Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.
import random

luvut = []
AK = int(input("Anna arpakuutioiden määrä: "))
for i in range(AK):
        luku = random.randint(1,6)
        luvut.append(luku)
print(f"Arpakuutioiden silmälukujen summaksi tuli: {sum(luvut)}.")
