import math

# Výpočet druhé mocniny
def rovnice(x):
    return x*x

# Výpočet druhé a třetí mocniny
def mocniny(x):
    druha = math.pow(x, 2)
    treti = math.pow(x, 3)
    return [druha, treti]

# Platnost proměnných
def platnost():
    global venku
    venku = 7
    return venku

# Volání funkce rovnice
for i in range(20):
    print(rovnice(i))

# Volání funkce mocniny
vys = mocniny(2)
print("{0} {1}".format(*vys)) # Identické s vys[0], vys[1]

# Volání funkce platnost
venku = 2
print(platnost())
print(venku)

input()
