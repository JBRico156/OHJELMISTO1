#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
#Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

lista = []
luku = input("Anna luku(tyhjämerkkijono lopettaa ohjelman): ")
while luku != "":
    luku = int(luku)
    lista.append(luku)
    luku = input("Anna luku(tyhjämerkkijono lopettaa ohjelman): ")
suurimmat = sorted(lista[-5:])
suurimmat.reverse()
print(suurimmat)