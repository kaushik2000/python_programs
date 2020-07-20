# Exploring dictionaries
"""
dictionary = dict()
dictionary['age'] = 12
dictionary['course'] = 182

print(dictionary)

dictionary['age'] = dictionary['age'] + 12
print(dictionary['age'])
"""
# Constant dictionaries
my_bio = { 'name' : 'Kaushik', 'age' : 20, 'college' : 'Sastra' }
print("Entire dictionary:", my_bio)
print("The list of hasp-map/key-value pairs in a nested list form:", my_bio.items())
print("The list of keys:", my_bio.keys())
print("The list of values:", my_bio.values())

for key in my_bio.keys() : 
    print(key.capitalize(), ":", my_bio[key])

print('name' in my_bio, 'Kaushik' in my_bio)