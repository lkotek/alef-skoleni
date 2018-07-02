# Program pro demonstraci základního chování Pythonu

vstup = int(input("Zadejte celé číslo: "))

# Demonstrace základních operátorů a víceřádkových komentářů

vysledky = """
Zadané číslo vynásobené 5:\t {0}
Zadané číslo podělené 3:\t {1}
Zadané číslo podělené 3:\t {2} (celočíselně!)
Zadané číslo sečtené s 5:\t {3}
Zadané číslo odečtené od 5:\t {4}
Zadané číslo umocněné na druh.:\t {5}
Zadané číslo umocněné na třetí:\t {6}
""".format(
    vstup * 5,
    vstup / 3,
    vstup // 3, # Vrací celočíselný výsledek
    vstup + 5,
    5 - vstup,
    vstup**2,   # Lze použít i specializovanou funkci
    vstup**3
    )

print(vysledky)

# Demonstrace větvení -- použití více bloků 'if'

if vstup > 0:
    print("Vstup je větší než 0!")
if vstup > 5:
    print("Vstup je větší než 5!")
if vstup > 10:
    print("Vstup je větší než 10!")
else:   # Značí všechny jiné případy
    print("Vstup je menší nebo roven 0!")

# Spojení '\n' je znak nového řádku, podobné jako '\t' tabulátoru
print("\nToto je prostý předěl :-)\n")

# Demonstrace větvení -- použití struktury 'if -- elif -- else'

if vstup > 0:
    print("Vstup je větší než 0!")
elif vstup > 5:
    print("Vstup je větší než 5!")
elif vstup > 10:
    print("Vstup je větší než 10!")
else:   # Značí všechny jiné případy
    print("Vstup je menší nebo roven 0!")

# Operátory rovnosti a nerovnosti, která situace je vhodnější?

rovnost = "Vstup se rovná 20."
nerovnost = "Vstup se nerovná 20."

if vstup == 20:
    print(rovnost)
if vstup != 20:
    print(nerovnost)

# Ano, jistě druhá :-)

if vstup == 20:
    print(rovnost)
else:
    print(nerovnost)

popis = "Vstup je v rozsahu 0 až 100."

# Následující zápisy jsou analogické

if vstup >= 0 and vstup <= 100:   # Klasický zápis
    print(popis)
    
if 0 <= vstup <= 100:             # Krásný pythonní zápis
    print(popis)

if vstup >= 0:               # Otrocký, ale správný zápis,
    if vstup <= 100:         # jsou situace, kdy je vhodný.
        print(popis)
          
input() 

