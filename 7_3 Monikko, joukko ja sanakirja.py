#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
#Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
#Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
#Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa,
#ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti,
#kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
#Löydät koodeja helposti selaimen avulla.)

lentoasemat = {}

while True:
    komento = int(input("Haluatko syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa?"
                    "1 = Uusi lentoasema, 2 = Hae olemassa olevan lentoaseman tiedot, 3 = Lopeta: "))

    if komento == 1:
        ICAO = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[ICAO] = nimi

    if komento == 2:
        avain = input("Anna ICAO-koodi: ")
        if avain in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[avain]}.")

    if komento == 3:
        break
