from fruitmand import fruitmand
import random

kies = input("Kies een aantal. ")

for i in range(int(kies)):
    print(fruitmand[random.randint(0, len(fruitmand) - 1)]['name'])
    random.shuffle(fruitmand)