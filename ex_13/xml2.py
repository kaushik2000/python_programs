import xml.etree.ElementTree as ET

data = '''<stuff>
            <users>
                <user x="2">
                    <id>001</id>
                    <name>Kaushik</name>
                </user>
                <user x="7">
                    <id>009</id>
                    <name>Kausthub</name>
                </user>
            </users>
        </stuff>'''
    
stuff_tree = ET.fromstring(data)

user_lst = stuff_tree.findall('users/user')
for user in user_lst :
    print("Name:", user.find("name").text)
    print("ID:", user.find("id").text)
    print("Attribute:", user.get("x"))
