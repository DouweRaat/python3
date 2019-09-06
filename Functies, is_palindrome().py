def reverse_string(woord):
    nieuw_woord = ""
    for i in range(len(woord)):
        nieuw_woord = woord[i] + nieuw_woord
    if nieuw_woord == woord:
        return True
    else:
        return False

print(reverse_string(str(input())))