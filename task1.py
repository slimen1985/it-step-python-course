import xml.etree.ElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root, "doc")
field1 = ET.SubElement(doc, "field1").text = "val1"
field2 = ET.SubElement(doc, "field2").text = "val2"

tree = ET.ElementTree(root)
tree.write("example.xml")
