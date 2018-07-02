#!/usr/bin/env python3

cetnost = {} # Slovník pro uložení statistiky

data = open("cetnost.txt", "r")

for znak in data.read():
    if znak in cetnost: # Existuje už záznam ve slovníku?
        cetnost[znak] += 1
    else:
        cetnost.update({znak:1})

data.close()

# Výpis dat
for klic in sorted(cetnost):
    print("{0} ... {1}x".format(klic, cetnost[klic]))
