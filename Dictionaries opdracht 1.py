getallen = {"0": "10", "1": "20", "2": "30", "3": "40", "4": "50", "5": "60"}

while True:
    getal = input()
    if getal == "quit":
        break
    else:
        print(getallen[getal])
