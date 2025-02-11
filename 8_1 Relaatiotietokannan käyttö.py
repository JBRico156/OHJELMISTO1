"""Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin. Ohjelma hakee ja tulostaa koodia vastaavan
lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen."""


import mysql.connector


def hae_lentokenttä(ICAO):
    sql = f"SELECT name, municipality FROM airport where ident='{ICAO}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if len(tulos) < 1:
        return print(f"Lentokenttää ei löydy ICAO-koodilla: {ICAO}")
    return print(f"ICAO-koodi: {ICAO}, kuuluu lentokentälle: {tulos[0][0]} ja se sijaitsee kunnassa {tulos[0][1]}.")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='jan',
         password='KevytSalasana2',
         autocommit=True
         )

ICAO = input("Syötä lentokentän ICAO-koodi: ")
hae_lentokenttä(ICAO)