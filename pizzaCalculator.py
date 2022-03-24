# Matthijs Raatgever PizzaCalculator

from cgitb import small
from re import I


largePizza = 12.00
mediumPizza = 7.00
smallPizza = 4.00
smallAmount = 0 
mediumAmount = 0
largeAmount = 0

prijzen ="""-------------------------
| Large pizza  : 12.00  |
| Medium pizza : 7.00   |
| Small pizza  : 4.00   |
-------------------------"""

def bestel():
    global largeAmount, mediumAmount, smallAmount
    i = True
    print(prijzen)
    pizzaInput = input("Welke grootte pizza wilt u? ").lower()
    while i:
        try:
            pizzaAmount = int(input(f"Hoeveel {pizzaInput} pizza's wilt u? "))
        except ValueError:
            print("Dat is geen geldig aantal")
        else:
            i = False
    
    if pizzaInput == "small":
        smallAmount += pizzaAmount
    elif pizzaInput == "medium":
        mediumAmount += pizzaAmount
    elif pizzaInput == "large":
        largeAmount += pizzaAmount

    nogmaals()

def nogmaals():
    nogmaals = input("Wilt u nog meer bestellen? ").lower()
    if nogmaals == "ja":
        bestel()
    else:
        bon()

def bon():
    global largeAmount, mediumAmount, smallAmount
    totaal = (largeAmount*largePizza) + (mediumAmount*mediumPizza) + (smallAmount*smallPizza)
    print("---------------------------")
    if largeAmount > 0:
        print(f" {largeAmount}x Large Pizza   : {largeAmount*largePizza}")
    if mediumAmount > 0:
        print(f" {mediumAmount}x Medium Pizza : {mediumAmount*mediumPizza}")
    if smallAmount > 0:
        print(f" {smallAmount}x Small Pizza   : {smallAmount*smallPizza}")
    print(f" Totaal           : {totaal}")
    print("---------------------------")


bestel()