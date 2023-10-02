xp = 0
yp = 1
idx = 0
nwd = 1


def extended_ea(a, b):
    global xp, yp, idx, nwd
    if b != 0:
        extended_ea(b, a%b)
        if idx != 0:
            x = yp
            yp = xp - int(a/b) * yp
            xp = x
        else:
            nwd = b
            idx += 1


a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
extended_ea(a, b)
print(f"{nwd} = {xp} * {a} + {yp} * {b}")