def max_van_3(getal1, getal2, getal3):
    list = [getal1, getal2, getal3]
    list.sort()
    hoogstegetal = list[-1]
    return hoogstegetal

print(max_van_3(int(input()), int(input()), int(input())))