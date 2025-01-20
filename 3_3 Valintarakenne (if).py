#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
#Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

    #Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
    #Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sp = str(input("Kerro biologinen sukupuolesi: "))
hg = int(input("Anna hemoglobiiniarvosi: "))

if sp == "mies":
    if hg < 134:
        print("hemoglobiiniarvo on alhainen")
    if hg > 133 and hg < 196:
        print("hemoglobiiniarvo on normaali")
    if hg > 195:
        print("hemoglobiiniarvo on korkea")

if sp == "nainen":
    if hg < 117:
        print("hemoglobiiniarvo on alhainen")
    if hg > 116 and hg < 177:
        print("hemoglobiiniarvo on normaali")
    if hg > 176:
        print("hemoglobiiniarvo on korkea")
