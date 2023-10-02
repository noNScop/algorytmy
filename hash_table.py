voted = {}


def check_voter(name):
    if voted.get(name):
        print("Pogonić go!")
    else:
        voted[name] = True
        print("Niech zagłosuje!")


while True:
    name = input("Jak się nazywasz? ")
    check_voter(name)