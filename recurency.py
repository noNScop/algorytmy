def bye():
    print("OK, cześć!")


def greet2(name):
    print(f"Jak sie masz, {name}?")


def greet(name):
    print(f"Cześć, {name}!")
    greet2(name)
    print("Przygotowanie do pożegnania...")
    bye()


greet("Karol")