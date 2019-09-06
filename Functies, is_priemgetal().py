def is_priemgetal(getal):
    if getal > 1:
        for i in range(2,getal):
            if getal % i == 0:
                return i
        else:
            return True
    else:
        return "Voer een hoger getal in."
print(is_priemgetal(int(input())))