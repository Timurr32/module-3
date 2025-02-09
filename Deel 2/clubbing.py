PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ("cola", "bier", "champagne")
VIP_LIST = ("jeroen", "jouke", "rudi")

leeftijd = input("Hoe oud ben je? ").strip()

age = int(leeftijd)
if age < 18:
    print("Helaas, je bent nog te jong voor de club.")
    print(f"Probeer het over {18 - age} jaar nog eens.")
    exit()

naam = input("Wat is je naam? ").strip().lower()

if age >= 21:
    bandje = "blauw"
else:
    bandje = "rood"

if naam in VIP_LIST:
    print(f"Je krijgt van mij een {bandje} bandje.")
else:
    if age >= 18:
        print("Je krijgt van mij een stempel.")
    else:
        print("Sorry, je mag niet naar binnen.")
        exit()

def bestellen():
    drinken = input("Wat wil je drinken (cola, bier, champagne)? ").strip().lower()

    if drinken not in DRANKJES:
        print("Sorry, geen idee wat je bedoelt. Hier een glaasje water.")
        exit()

    if drinken == "cola":
        if bandje == "blauw":
            print("Alstublieft, complimenten van het huis.")
        else:
            print(f"Alsjeblieft, je cola kost {PRIJS_COLA} euro.")

    elif drinken == "bier":
        if bandje == "rood":
            print("Sorry, je mag geen alcohol bestellen onder de 21.")
            exit()
        elif naam in VIP_LIST:
            print("Alstublieft, complimenten van het huis.")
        else:
            print(f"Alsjeblieft, je bier kost {PRIJS_BIER} euro.")

    elif drinken == "champagne":
        if bandje != "blauw" or naam not in VIP_LIST:
            print("Sorry, alleen VIP's van 21 jaar en ouder mogen champagne bestellen.")
            exit()
        else:
            print(f"Alsjeblieft, je champagne kost {PRIJS_CHAMPAGNE} euro.")

bestellen()
