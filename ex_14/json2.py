# Using json library in python
import json

data = '''[
    {
        "name" : "Kaushik",
        "id" : "1",
        "x" : "13"
    },
    {
        "name" : "kihsuaK",
        "id" : "99",
        "x" : "31"
    }
    ]'''

info = json.loads(data)
print("User count:", len(info))
for item in info :
    print("Name:",item["name"])
    print("ID:",item["id"])
    print("X-value:",item["x"])
