#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
#Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
#syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
#mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.


import random

def noppa_peli(tahko):
    numero = 0
    while numero != tahko:
        numero = random.randint(1, tahko)
        print(numero)

tahko = int(input(("Anna nopan tahkojen määrä: ")))
noppa_peli(tahko)
