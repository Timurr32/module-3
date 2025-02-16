from fruitmand import fruitmand

beschikbare_kleuren = ['yellow', 'green', 'orange', 'red', 'brown']

while True:
    kleur = input("Kies een kleur: (beschikbare kleuren zijn geel, groen, oranje, rood, bruin) ").lower()
    if kleur in beschikbare_kleuren:
        break
    else:
        print(f"De kleur {kleur} zit er niet in de fruitmand. Probeer het opnieuw.")

print(f"Je hebt de kleur {kleur} gekozen.")

ronde_vruchten = 0
niet_ronde_vruchten = 0

for fruit in fruitmand:
    if fruit["color"] == kleur:
        if fruit["round"]:
            ronde_vruchten += 1
        else:
            niet_ronde_vruchten += 1

if ronde_vruchten > niet_ronde_vruchten:
    verschil = ronde_vruchten - niet_ronde_vruchten
    print(f"Er zijn {verschil} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}.")
else:
    print(f"Er zijn niet meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}.")