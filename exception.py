getal = input("Vul eens een getal hier in, maakt niet uit welk getal ")

try:
    getal = float(getal)
except ValueError:
    print("Gast, ik zei vul een nummer in")
else:
    print("Lekker bezig!")
finally:
    exit()