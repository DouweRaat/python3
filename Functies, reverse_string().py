def reverse_string(woord):
    nieuw_woord = ""
    for i in range(len(woord)):
        nieuw_woord = woord[i] + nieuw_woord
    return nieuw_woord

print(reverse_string(str(input())))