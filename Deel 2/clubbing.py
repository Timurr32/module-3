PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

#bouw hieronder de floowchart na

leeftijd = input("Hoe oud ben je? ").lower()
age = int(leeftijd)
if age < 18:
    print("Helaas, je bent nog te jong voor de club.")
    print(f"Probeer het in in {18 - age} jaar nog eens.")
    exit()
elif age >= 18:
    naam = input("Wat is je naam? ").lower()

if age > 21:
    leeftijdboven21 = True
    bandje = "blauw"
else:
    leeftijdboven21 = False
    bandje = "rood"



if naam.lower() in VIP_LIST and leeftijdboven21:
    print(f"Je krijgt van mij een {bandje} bandje")

elif naam.lower() in VIP_LIST and not leeftijdboven21:
    print(f"Je krijgt van mij een {bandje} bandje")

elif naam.lower() not in VIP_LIST and leeftijdboven21:
    print(f"Je krijgt van mij een stempel")

elif naam.lower() not in VIP_LIST and not leeftijdboven21:
    pass




def bestellen():
    drinken = input("Welk drankje wilt u bestellen? ").lower()
    while True:
        if drinken == 'cola':
            if bandje == "blauw":
                print("Alstublieft, complimenten van het huis.")
                exit()
            else:
                print(f"Alsjeblieft je {drinken} dat is dan {PRIJS_COLA} euro.")
            break
        elif drinken == 'bier':
            print(f"Dat kost dan {PRIJS_BIER} euro.")
            
            break
        elif drinken == 'champagne':
            print(f"Dat kost dan {PRIJS_CHAMPAGNE} euro.")
            break
        else:
            print("Sorry geen idee wat je bedoeld, hier een glaasje water.")
            exit()

bestellen()

