#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
#Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm
cm = 2.54
tuuma = 1
while tuuma >= 0:
    tuuma = int(input("Anna tuuma määrä(negatiivinen luku lopettaa ohjelman): "))
    if tuuma < 0:
        break
    print(f"{tuuma} tuumaa on {tuuma * cm} senttimetriä")
print("Kiitos ja näkemiin!")
