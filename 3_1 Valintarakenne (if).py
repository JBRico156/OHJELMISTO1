#Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# #Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# #montako senttiä alimmasta sallitusta pyyntimitasta puuttuu. Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuha = int(input("Kuinka pitkä kuha on senttimetreinä?: "))
if kuha < 37:
    print(f"Laske kuha takaisin järveen. Kuha on {37 - kuha} senttiä alle sallitun pyyntimitan.")
else:
    print("Vau! komia kuha! Onnea!")