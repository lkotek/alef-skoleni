#!/usr/bin/env python3

# Víceřídkový komentář (multiline string)
"""
slova = input("Zadej slova oddělená mezerami: ").split()
# print(slova)

for i in slova:
    #print(i, end=" ")
    for pismeno in i:
        print(pismeno, end=" ")    

# print(" ".join(slova))
"""

# Demonstrace práce se seznamem
seznam = ["ahoj", "jak", "jde"]
print("{0} {1} {2}".format(seznam[0], seznam[1], seznam[2]))
print("{0} {1} {2}".format(*seznam))

"""
for x in range(len(seznam)):
    print(seznam[x])
"""

# Demonstrace práce se slovníkem
slovnik = {"a": 7, "b": 54, "c":"Nohy"}

for klic in slovnik:
    print("{0} ... {1}".format(
        klic,
        slovnik[klic]
        )
          )
