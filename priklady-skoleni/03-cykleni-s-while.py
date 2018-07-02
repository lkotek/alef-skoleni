#!/usr/bin/env python3

import os

x = 0

nazev = "soubor.txt"
velikost = 0

# Demonstrace cyklu while a zápisu do souboru

"""
soubor = open(nazev, "w")
print(os.getcwd())

input()

while True:
    #x = x + 1
    x += 1
    print(soubor.tell())
    soubor.write(str(x))    
    if soubor.tell() > 1000:
        break

soubor.close()
"""

# Alternativní zpsůob práce se souborem s direktivou with

with open(nazev, "w") as soubor:
    print(os.getcwd())
    input("Stiskněte ENTER...")
    while True:
        # Dlouhý a zkrácený zápis inkrementace čísla
        #x = x + 1
        x += 1
        print(soubor.tell()) # Aktuální velikost souboru
        soubor.write(str(x))
        # Ukončení zapisování při dosažení velikosti 1000 B
        if soubor.tell() > 1000:
            break

