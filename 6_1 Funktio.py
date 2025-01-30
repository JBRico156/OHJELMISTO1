#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
#Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
#Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def noppa_peli():
    numero = 0
    while numero != 6:
        numero = random.randint(1, 6)
        print(numero)

noppa_peli()





