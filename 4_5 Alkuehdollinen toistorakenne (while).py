#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
#Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
#Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
#Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
#(Oikea käyttäjätunnus on python ja salasana rules).

oikea_tunnus = "python"
oikea_salasana = "rules"
yritykset = 0
tunnus = ""
salasana = ""

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    if tunnus != oikea_tunnus or salasana != oikea_salasana:
        print("Pääsy evätty")
        yritykset += 1








