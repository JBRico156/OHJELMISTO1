#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
#Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
#syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan
#allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()
nimi = " "
while nimi != "":
    nimi = str(input("Anna nimi: "))
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    if nimi not in nimet:
        print("Uusi nimi")
    nimet.add(nimi)
print("Nimet ovat: ")
for i in nimet:
    print(i)
