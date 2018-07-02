#!/usr/bin/env python3

# Demonstrace funkčí a práce s moduly

import modul

a = 8

def funkce(a=6):
    return a**2

print(funkce())
print(funkce(7))

print(a)

modul.funkce_dva()
