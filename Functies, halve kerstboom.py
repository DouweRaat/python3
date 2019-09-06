def halvekerstboom(woord):
    for i in range(len(woord)):
        a = i + 1
        letters = woord[i] * a
        print(letters)

halvekerstboom(input())