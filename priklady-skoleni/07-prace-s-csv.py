#!/usr/bin/env python3

# Vytažení dat ze souboru CSV a přeuložení s jinou strukturou
# (Dlouhá varianta)

csv = open("python.txt", "r")
target = []

for radek in csv.readlines():
    source = radek.split(",")
    target.append("{0},{1}".format(source[2], source[4]))
    
csv.close()

print(target)

to_write = open("target.txt", "w")
for zapis in target:
    to_write.write(zapis + "\n")    

to_write.close()
