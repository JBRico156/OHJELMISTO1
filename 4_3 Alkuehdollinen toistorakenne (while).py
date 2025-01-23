#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.
luvut = []
luku = 0
while luku != "":
    luku = (input("Anna luku: "))
    if luku == "":
        break
    numero = int(luku)
    luvut.append(numero)
    isoin = max(luvut)
    pienin = min(luvut)
print(f"pienin luku on {pienin} ja suurin luku on {isoin}")
