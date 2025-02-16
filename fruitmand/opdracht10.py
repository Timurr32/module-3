from fruitmand import fruitmand

sorted_fruitmand = sorted(fruitmand, key=lambda fruit: fruit['weight'], reverse=True)

for fruit in sorted_fruitmand:
    print(fruit['name'], "=" ,fruit["weight"] / 1000, "kg")