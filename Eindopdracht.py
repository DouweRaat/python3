def readfile():
    with open('Eindopdrachttext.txt') as f:
      bestandsdata = f.read().split('\n')

    boodschappenlijstje = {}

    for item in bestandsdata:
        if not item == '':
            woord1, woord2 = item.split("=")
            boodschappenlijstje[woord1] = woord2
    return boodschappenlijstje

def menu():
    print("\nToets '1' om een product met de prijs aan het boodschappenlijstje toe te voegen.\nToets '2' om een product te verwijderen.\nToets '3' om uw al toegevoegde producten te bekijken.\nToets '0' om het programma af te sluiten.")
    keuze = input("Voer hier uw opdracht in: ")
    if keuze == "1":
        toevoegen()
    elif keuze == "2":
        verwijderen()
    elif keuze == "3":
        showall()
    elif keuze == "0":
        quitprogram()
    else:
        print("\nVoer één van de aangegeven toetsen in.\n")
        menu()

def toevoegen():
    addkey = input("\nProduct: ")
    addvalue = input("Prijs: ")
    with open('Eindopdrachttext.txt', 'a') as f:
        f.write(addkey + "=" + addvalue + "\n")
    menu()

def verwijderen():
    boodschappenlijstje = readfile()
    deletekey = input("\nProduct: ")
    if deletekey in boodschappenlijstje:
        del boodschappenlijstje[deletekey]
        with open('Eindopdrachttext.txt', 'w') as f:
            for item in boodschappenlijstje:
                f.write(item + "=" + boodschappenlijstje[item] + "\n")
    else:
        print("Dit product bestaat niet.")
    menu()

def showall():
    print("\n")
    boodschappenlijstje = readfile()
    for key, value in boodschappenlijstje.items():
        print(key, value)
    menu()

def quitprogram():
    print("")


menu()