#!/usr/bin/env python3

# Tvořený příklad na spouštění programů z OS a načtení vrácených hodnot

import subprocess

source = "/etc/hosts"
nazev = open(source, "r")

for zaznam in nazev:
    ip = zaznam.split()[0]
    print(ip)
    p = subprocess.Popen(["ping", "-c", "1", ip], stdout=subprocess.PIPE)
    o, e = p.communicate()
    print(o)

nazev.close()

