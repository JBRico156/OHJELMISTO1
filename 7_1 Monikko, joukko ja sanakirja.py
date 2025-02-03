#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
#(kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
#Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

talvi = ("joulukuu", "tammikuu", "helmikuu")
kevät = ("maaliskuu", "huhtikuu", "toukokuu")
kesä = ("kesäkuu", "heinäkuu", "elokuu")
syksy = ("syyskuu", "lokakuu", "marraskuu")

numero = int(input("Anna kuukauden numero: "))

if numero >= 3 and numero <= 5:
    print(f"Nyt on kevät ja on {kevät[numero - 3]}")
elif numero >= 6 and numero <= 8:
    print(f"Nyt on kesä ja on {kesä[numero - 6]}")
elif numero >= 9 and numero <= 11:
    print(f"Nyt on syksy ja on {syksy[numero - 9]}")
elif numero >= 1 and numero <= 2:
    print(f"Nyt on talvi ja on {talvi[numero]}")
elif numero == 12:
    print(f"Nyt on talvi ja on {talvi[0]}")











