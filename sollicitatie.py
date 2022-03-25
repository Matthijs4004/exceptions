# Sollicitatie Ruimtevuilnisman

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("+        Sollicitatie formulier Circus directeur         +")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Er wordt u een aantal relevante vragen gesteld...")
print("Gelieve die naar eer en geweten in te vullen.")
print("Als blijkst dat u aan de criteria voldoet dan komt u in")
print("aanmerking voor een serieus solliciatiegesprek!")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

naam = input("Wat is uw naam? ")
bestetekst = "Beste " + naam + ","
faaltekst = "U voldoet niet aan onze strenge eisen voor de functie van Circus directeur, het spijt ons!"
geslaagdtekst = "Proficiat! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV."

dressuur = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
jongleren = int(input("Hoeveel jaar praktijkervaring heeft u met jongleren? "))
acrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? "))
lichaamslengte = int(input("Wat is uw netto lichaamslengte in hele cm, dus exclusief uw kapsel? "))
if lichaamslengte > 272:
    raise ValueError("On... mogelijk, dan zou jij de langste persoon in de wereld moeten zijn?!?!?! ")
lichaamsgewicht = int(input("Wat is uw lichaamsgewicht in hele kg? "))
if lichaamsgewicht > 800:
    raise ValueError("Gozer, niemand is zwaarder dan 800 kg")
diploma = input("Bent u in het bezit van een diploma MBO-4 ondernemen? Ja/Nee ")
hogehoed = input("Bent u in het bezit van een hoge hoed? Ja/Nee ")
rijbewijs = input("Bent u in het bezit van een geldig vrachtwagen rijbewijs? Ja/Nee ")
certificaat = input("Bent u in het bezit van het Certificaat “Overleven met gevaarlijk personeel”? Ja/Nee ")
geslacht = input("Welke geslacht bent u? (man/vrouw) ")

if geslacht.lower().strip() == "man":
    snor = input("Heeft u een snor? Ja/Nee ")
    if snor.lower().strip() == "ja":
        snorB = int(input("Hoe breed is uw snow? "))
        if snorB > 100:
            raise ValueError("Pffff leugenaar, hoe kan iemand nou een snor van 100cm groeien. ONMOGELIJK!")
elif geslacht.lower().strip() == "vrouw":
    krulhaar = input("Draagt u rood krulhaar? Ja/Nee ")
    if krulhaar.lower().strip() == "ja":
        krulhaarL = input("Is uw rood krulhaar langer dan 20cm? Ja/Nee ")

if dressuur > 4 or jongleren > 5 or acrobatiek > 3 or lichaamsgewicht > 150 and lichaamsgewicht > 90 and diploma.lower().strip() == "ja" and hogehoed.lower().strip() == "ja" and rijbewijs.lower().strip() == "ja" and certificaat.lower().strip() == "ja" or snorB > 10 or krulhaarL.lower().strip() == "ja":
    print(bestetekst)
    print(geslaagdtekst)
else:
    print(bestetekst)
    print(faaltekst)