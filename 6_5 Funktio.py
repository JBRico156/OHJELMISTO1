#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa toisen listan,
#joka on muuten samanlainen kuin parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
#Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen
#että karsitun listan.

def parittomat(lista):
    parilliset = []
    for i in lista:
        if i % 2 == 0:
            parilliset.append(i)
    return parilliset

lista = [1, 3, 4, 7, 5, 6, 3, 5, 12, 11, 10, 8, 1]
parittomat(lista)
print(f"Alkuperäinen lista: {lista}.")
print(f"Listan parilliset luvut: {parittomat(lista)}.")
