#!/usr/bin/env python3

jmeno = input("Zadej jméno: ")

# Ošetření vstupu pomocí výjimek
try:
    vek = int(input("Zadej věk: ")) # Přetypování na řetězec
except:
    print("Chtěl jsem číslo.")
    exit(1)


# Výpisy proměnných přes spojování řetězce a metodu format
# print("Uživatel "+jmeno+" je starý "+vek+" let.")
print("Uživatel je {0} starý {1} let.".format(
    jmeno,
    vek)
      )

# Demostrace větvení
if vek >= 18:
    print("Jsi plnoletý")
if vek >= 18 and vek <= 65:
    print("Patrně pracuješ.")
else:
    print(":-(")
