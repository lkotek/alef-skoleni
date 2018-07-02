import urllib.request

web = urllib.request.urlopen("http://www.root.cz")
dokument = web.read()
data = dokument.decode("utf-8")	# Predpokladame utf-8

print(type(data))
print(data)
print(web.getcode())	# Zjisti vysledny http kod
