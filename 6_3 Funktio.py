#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa
#paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
#Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.

#Yksi gallona on 3,785 litraa.

def muunnin(gallona):
    litra = gallona * 3.785
    print(f"{litra:.2f}")

gallona = 0
while gallona >= 0:
    gallona = float(input("Anna gallona määrä, joka muutetaan lirtoiksi(negatiivinen luku pysäyttää ohjelman): "))
    if gallona < 0:
        break
    muunnin(gallona)
print("Kiitos ja näkemiin!")



