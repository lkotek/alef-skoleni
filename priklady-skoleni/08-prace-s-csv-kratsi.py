#!/usr/bin/env python3

# Vytažení dat ze souboru CSV a přeuložení s jinou strukturou
# (Krátká varianta)

csv = open("PYTHON.txt", "r")
to_write = open("target.txt", "w")

for radek in csv.readlines():
    source = radek.split(",")
    to_write.write("{0},{1}\n".format(source[2], source[4]))
    
csv.close()
to_write.close()
