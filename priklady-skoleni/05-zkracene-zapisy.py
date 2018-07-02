# Syntaktický cukr
"""
Program odvozen z:
http://www.sallyx.org/sally/python/syntakticky-cukr.php
"""

# Zkrácený zápis podmínky zkombinovaný s přiřazením
prom = 1 if True else 0
print prom

# Zkrácený zápis cyklu (vytvoření seznamu)
print [x**2 for x in range(5)]

# Zkrácený zápis cyklu (vytvoření seznamu) s podmínkou
print [x**2 for x in range(5) if x != 3]

# Dva for cykly (vytvoření seznamu)
print [i*j for i in range(4) for j in range(4)]

# Dva for cykly (vytvoření matice naplněné nulami)
print [[0 for i in range(4)] for j in range(4)]

