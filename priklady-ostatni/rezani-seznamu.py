# Řezání seznamů v Pythonu

# Pracovní řetězec
retezec = "ahoj svete"

# Indexace prvního a posledního prvku
print(retezec[0], retezec[-1])

# První řezání od pozice (včetně) do další pozice (mimo)
print(retezec[3:5])

# Druhé řezání od začátku do pozice
print(retezec[:5])

# Třetí řezání od pozice do konce
print(retezec[5:])

# Čtvrté řezání - nahrazení úseku
cisla = [1,2,4,8,16,32,64,128]
cisla[4:4] = [7]    # Analogie k metodě insert
print(cisla)

# Čtvrté řezání - vložení na místo
cisla = [1,2,4,8,16,32,64,128]
cisla[0:4] = [7]
print(cisla)

# Jak rozložit polynom na jendotlivé prvky..?
x = 7   # Zadaná hodnota proměnné 'x'
r = "2*x*x*x + 4*x*x + 7*x + 5"
vysledek = 0
for vyraz in r.split("+"):
    mezi_vysledek = 1
    for prvek in vyraz.split("*"):
        mezi_vysledek *= int(
            prvek.strip().replace("x", str(x))
            )
    vysledek += mezi_vysledek

print(vysledek)
input()




    



