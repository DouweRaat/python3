getallen = {"0": "10", "1": "20", "2": "30", "3": "40", "4": "50", "5": "60"}

while True:
    getal = input()
    if getal == "add":
        addkey = input("Key: ")
        addvalue = input("Value: ")
        getallen[addkey] = addvalue
    elif getal == "delete":
        deletekey = input("Key: ")
        if deletekey in getallen:
            del getallen[deletekey]
        else:
            print("Deze key bestaat niet.")
    elif getal == "all":
        for key, value in getallen.items():
            print(key, value)
    elif getal == "quit":
        break
    else:
        if getal in getallen:
            print(getallen[getal])
        else:
            print("Deze key bestaat niet.")