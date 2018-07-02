import xml.etree.ElementTree as XML

strom = XML.parse("data.xml")
print(type(strom))
print(strom)
struktura = strom.getroot()

for zaznam in struktura:
    print(zaznam.tag)		# Pristup k datum
    print(zaznam.attrib)
