class partymember():
    x = 0
    name = ""

    # Constructor
    def __init__(self, name):
        self.name = name
        print('Object is constructed')

    def count(self):
        self.x = self.x + 1
        print('Count so far:', self.x)
    
class sportsfan(partymember):
    points = 0

    def touchdown(self):
        self.points = 70
        self.count()
        print('Points so far:', self.x)

s = partymember("Sally")
s.count()
s.count()

j = sportsfan("John")
j.count()
j.touchdown()
