# Creating user-defined classes OOP
class person():
    x = 0

    # Constructor
    def __init__(self):
        print('Object is constructed')

    def count(self):
        self.x = self.x + 1
        print('Count so far:', self.x)
    
    # Destructor
    def __del__(self):
        print('Object is destructed')
    
a = person()
a.count()
a.count()

print("Object-type:", type(a))
print("Object attributes and methods:", dir(a))