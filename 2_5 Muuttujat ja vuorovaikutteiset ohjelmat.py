luoti = 13.3
naula = 425.6
leiviskä = 8512

leiviskät = float(input("Anna leiviskät.\n"))
print(" ")
naulat = float(input("Anna naulat.\n"))
print(" ")
luodit = float(input("Anna luodit.\n"))
print(" ")

leipä = leiviskä * leiviskät
naula_1 = naula * naulat
luoti_1 = luoti * luodit
paino = (leipä + naula_1 + luoti_1)
paino_kg = (leipä + naula_1 + luoti_1) // 1000
grammat = paino % 1000

print("Massa nykymittojen mukaan:")
print(f"{paino_kg:.0f} kilogrammaa ja {grammat:.0f} grammaa.")
