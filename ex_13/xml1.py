import xml.etree.ElementTree as ET
# Create local XML data to experiment on
data  = '''<person> 
            <name>Kaushik</name>
            <phone type="integer">
                +917598118957
            </phone>
            <email hide="yes"/>
        </person>'''

# Create XML tree
tree = ET.fromstring(data)

print("Name:", tree.find('name').text)
print("Phone number:", tree.find('phone').text.strip(), "Type:", tree.find('phone').get('type'))
print("E-mail attribute:", tree.find('email').get('hide'))
