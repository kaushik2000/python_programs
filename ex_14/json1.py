# Using json library in python
import json

data = '''{
    "name" : "Kaushik",
    "phone" : {
        "type" : "int1",
        "number" : "+1 234 567 890"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)
print("Name:", info["name"])
print("Phone:", info["phone"]["number"])
print("Hide:", info["email"]["hide"])
