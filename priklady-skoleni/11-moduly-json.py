import json

# Nacteni bezneho textoveho souboru obsahujiciho JSON

zdroj = open("data.json", "r", encoding="utf-8")
data = json.load(zdroj)	# Prevedeni na JSON
zdroj.close()

print(type(data))
print(data)
