def readfile():
    with open(r"C:\Users\Gebruiker\Desktop\School\Coderclass\Python\Python 3\python3\Eindopdrachttext.txt") as f:
      bestandsdata = f.read().split('\n')

    boodschappenlijstje = {}

    for item in bestandsdata:
        if not item == '':
            woord1, woord2 = item.split("=")
            boodschappenlijstje[woord1] = woord2
    return boodschappenlijstje

def main(boodschappenlijstje):
    close = False
    while close == False:
        print("\nToets '1' om een product met de prijs aan het boodschappenlijstje toe te voegen.\nToets '2' om een product te verwijderen.\nToets '3' om uw al toegevoegde producten te bekijken.\nToets '0' om het programma af te sluiten.")
        keuze = input("Voer hier uw opdracht in: ")
        if keuze == "1":
            toevoegen(boodschappenlijstje)
        elif keuze == "2":
            verwijderen(boodschappenlijstje)
        elif keuze == "3":
            showall(boodschappenlijstje)
        elif keuze == "0":
            quitprogram(boodschappenlijstje)
            close = True
        else:
            print("\nVoer één van de aangegeven toetsen in.")

def toevoegen(boodschappenlijstje):
    addkey = input("\nProduct: ")
    addvalue = input("Prijs: ")
    boodschappenlijstje[addkey] = addvalue

def verwijderen(boodschappenlijstje):
    deletekey = input("\nProduct: ")
    if deletekey in boodschappenlijstje:
        del boodschappenlijstje[deletekey]
    else:
        print("Dit product bestaat niet.")

def showall(boodschappenlijstje):
    if boodschappenlijstje == {}:
        print("\nEr staat niks in het boodschappenlijstje.")
    else:
        for key, value in boodschappenlijstje.items():
            print("\n", key, value)

def quitprogram(boodschappenlijstje):
    with open(r"C:\Users\Gebruiker\Desktop\School\Coderclass\Python\Python 3\python3\Eindopdrachttext.txt", 'w') as f:
        for item in boodschappenlijstje:
            f.write(item + "=" + boodschappenlijstje[item] + "\n")

boodschappenlijstje = readfile()
if __name__ == "__main__":
    main(boodschappenlijstje)