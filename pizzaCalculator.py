# Matthijs Raatgever PizzaCalculator

largePizza = 12.00
mediumPizza = 7.00
smallPizza = 4.00

# Dit is de kaart met alle prijzen per grootte van de pizza

print("-------------------------")
print("| Large pizza  : 12.00  |")
print("|                       |")
print("| Medium pizza : 7.00   |")
print("|                       |")
print("| Small pizza  : 4.00   |")
print("-------------------------")

# Invoer van hoeveel pizza's de klant wilt hebben

hoeveelLarge = int(input("Hoeveel large pizza's wilt u? "))
hoeveelMedium = int(input("Hoeveel medium pizza's wilt u? "))
hoeveelSmall = int(input("Hoeveel small pizza's wilt u? "))

# Lijstje van hoeveel pizza's de klant heeft besteld

print("Hoeveelheid large pizza's: ", hoeveelLarge)
print("Hoeveelheid medium pizza's: ", hoeveelMedium)
print("Hoeveelheid small pizza's: ", hoeveelSmall)

# De berekening van het totaal bedrag wat de klant moet betalen

bedrag = (hoeveelLarge * largePizza) + (hoeveelMedium * mediumPizza) + (hoeveelSmall * smallPizza)

factuurtekst = "U heeft voor " + str(bedrag) + " aan pizza's besteld."

print(factuurtekst)
