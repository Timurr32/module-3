def boodschappenlijstje():
    boodschappen = []
    
    while True:
        artikel = input("Welk artikel wilt u toevoegen? ").lower()
        aantal = input(f"Hoeveel {artikel} wilt u toevoegen? ")
        boodschappen.append(f"{aantal} {artikel}")
        
        keuze = input("Wilt u nog een artikel toevoegen? (ja/nee) ").lower()
        if keuze != "ja":
            break
    
    print("Boodschappenlijstje:")
    for item in boodschappen:
        print(f"- {item}")

boodschappenlijstje()
