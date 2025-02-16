from fruitmand import fruitmand


kleur_vertaling = {
    'yellow': 'geel',
    'green': 'groen',
    'orange': 'oranje',
    'red': 'rood',
    'brown': 'bruin'
}

langste_fruit = None
for fruit in fruitmand:
    if langste_fruit is None or len(fruit['name']) > len(langste_fruit['name']):
        langste_fruit = fruit

kleur_nederlands = kleur_vertaling[langste_fruit['color']]

print(f"De {langste_fruit['name']} ({kleur_nederlands}) weegt {langste_fruit['weight']} gram.")