#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
#Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def listan_summa(lista):
    summa = sum(lista)
    return summa

lista = [1, 3, 4, 7, 5]
listan_summa(lista)
print(f"Listan lukujen summa on {listan_summa(lista)}.")
