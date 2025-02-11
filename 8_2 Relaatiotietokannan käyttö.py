"""Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien
lentokenttien lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne."""


import mysql.connector


def hae_lentokenttä(maa):
    sql = f"SELECT type FROM airport where iso_country='{maa}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if len(tulos) < 1:
        return print(f"Lentokenttiä ei löydy maakoodilla: {maa}")
    pieni = []
    keski = []
    suuri = []
    heli = []
    suljettu = []
    for i in tulos:
        for x in i:
            if x == "closed":
                suljettu.append(i)
            if x == "heliport":
                heli.append(i)
            if x == "small_airport":
                pieni.append(i)
            if x == "medium_airport":
                keski.append(i)
            if x == "large_airport":
                suuri.append(i)
    return print(f"Maakoodilla: {maa} löytyy {len(tulos)} lentokenttää.\n"
                 f"Pieniä lentokenttiä löytyy {len(pieni)}.\n"
                 f"Keskikokoisia lentokenttiä löytyy {len(keski)}.\n"
                 f"Suuria lentokenttiä löytyy {len(suuri)}.\n"
                 f"Helikoptrikenttiä löytyy {len(heli)}.\n"
                 f"Suljettuja kenttiä löytyy {len(suljettu)}.")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='jan',
         password='KevytSalasana2',
         autocommit=True
         )

maa = input("Syötä lentokentän maakoodi: ")
hae_lentokenttä(maa)