#Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
#Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
#Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle
#(eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def pizza(halkaisija, hinta):
    sade = halkaisija / 2
    p_a = math.pi * sade ** 2 * 10 ** -2
    hinta_laatu = hinta / p_a
    return hinta_laatu

halkaisija = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
hinta = float(input("Anna ensimmäisen pizzan hinta euroina: "))
pizza1 = pizza(halkaisija, hinta)
halkaisija = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta = float(input("Anna toisen pizzan hinta euroina: "))
pizza2 = pizza(halkaisija, hinta)

if pizza1 < pizza2:
    print(f"Ensimmäinen pizza on halvempi, se maksaa {pizza1:.2f} euroa per neliömetri. Toinen pizza maksaa {pizza2 - pizza1:.2f} euroa enemmän per neliömetri.")
if pizza1 > pizza2:
    print(f"Toinen pizza on halvempi, se maksaa {pizza2:.2f} euroa per neliömetri. Ensimmäinen pizza maksaa {pizza1 - pizza2:.2f} euroa enemmän per neliömetri.")
if pizza1 == pizza2:
    print("Pizzat ovat yhtä hintavia.")


