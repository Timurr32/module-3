from fruitmand import fruitmand

fruitmand.remove(fruitmand[4])

kleuren = set()

for fruit in fruitmand:
    kleuren.add(fruit["color"])

for kleur in kleuren:
    print(kleur)
