"""Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä. Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
Asenna kirjasto valitsemalla View / Tool Windows / Python Packages. Kirjoita hakukenttään geopy ja vie asennus loppuun."""


import mysql.connector
from geopy.distance import geodesic


def hae_lentokenttä1(ICAO1):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport where ident='{ICAO1}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    sijainti1 = tulos
    if len(tulos) < 1:
        return print(f"Lentokenttää ei löydy ensimmäisellä ICAO-koodilla: {ICAO1}")
    return sijainti1

def hae_lentokenttä2(ICAO2):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport where ident='{ICAO2}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    sijainti2 = tulos
    if len(tulos) < 1:
        return print(f"Lentokenttää ei löydy toisella ICAO-koodilla: {ICAO2}")
    return sijainti2

def etäisyys(sijainti1, sijainti2):
    ICAO1 = sijainti1
    ICAO2 = sijainti2
    etäisyys_km = (geodesic(ICAO1, ICAO2).kilometers)
    print(f"Kenttien välinen etäisyys on {etäisyys_km:.0f} kilometriä.")

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='jan',
         password='KevytSalasana2',
         autocommit=True
         )

ICAO1 = input("Syötä ensimmäisen lentokentän ICAO-koodi: ")
ICAO2 = input("Syötä toisen lentokentän ICAO-koodi: ")
sijainti1 = hae_lentokenttä1(ICAO1)
sijainti2 = hae_lentokenttä2(ICAO2)

if sijainti1 == None or sijainti2 == None:
    print("Virhe syötteessä tarkista, että syötit oikeat ICAO-koodit")

elif len(sijainti1) > 0 and len(sijainti1) > 0:
    etäisyys(sijainti1, sijainti2)










