from lxml import etree

tree = etree.parse("example.xml")
root = tree.getroot()

# Search for all elements with the tag "field1"
field1_elements = root.xpath("//field1")
for element in field1_elements:
    print(element.text)

# Search for all elements with the tag "field2" and a parent tag of "doc"
field2_elements = root.xpath("//doc/field2")
for element in field2_elements:
    print(element.text)
