# Hádej číslo

# Modul pro náhodné generování čísel
import random

# Definice proměnných
myslene = random.randint(1,100)
pokus = 0
hadane = -1
konec = "Pro ukonceni zadejte cislo 0."

# Úvodní výzva programu
print("Hadej cele cislo mezi 1 a 100.")
print(konec)

# Ověřování uhodnutí čísla
while myslene != hadane:
    # Počet pokusů
    pokus += 1 # pokus = pokus + 1
    # Výjimka ošetřující nesprávný datový typ vstupu
    try:
        print("{0}. pokus".format(pokus))
        # Zadání a přiřazení hádaného čísla do proměnné
        hadane = int(input(u"Tvuj tip: "))
    except:
        # Ošetření výjimky
        print("Je nutne zadat cele cislo!")
        print(konec)
        # Není ubrán počet pokusů
        pokus -= 1
        continue

    # Ošetření možných situací
    if(hadane == 0):
        print("Ukoncuji.")
        exit()
    elif(myslene > hadane):
        print("> Pridej!")
    elif(myslene < hadane):
        print("> Uber!")        

print("\nUhodl jsi cislo {0} po {1} pokusech.".format(myslene, pokus))

input()
