o = []

# Naplnění matice pomocí kombinace cyklů for a while
for i in range(2):
    p = []
    c = 0
    while c < 2:
        try:
            x = int(input("Zadej cislo: "))
            p.append(x)
            o.append(p)
            c = c + 1
        except:
            print("To neděláš dobře...")

# Výpis seznamu klasická varianta
for k in o:
    for l in k:
        print(l)

# Výpis seznamu, zkrácený zápis
for m in o:
    print("1: {0} \t{1}".format(m[0], m[1]))

# Výpis seznamu specifický pro Python
for m in o:
    print("1: {0} \t{1}".format(*m))

input()

