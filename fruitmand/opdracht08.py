from fruitmand import fruitmand


fruitmand.append({"name": "watermeloen", "weight": 1500})

gewicht = 0

for fruit in fruitmand:
    gewicht += fruit["weight"]



print(gewicht)