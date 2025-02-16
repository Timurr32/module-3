from fruitmand import fruitmand


gewicht = 0

for fruit in fruitmand:
    gewicht += fruit["weight"]

print(gewicht)