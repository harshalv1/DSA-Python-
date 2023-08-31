import sys

class Warrior:
    def __init__(self, health):
        self.health = health

warrior1 = Warrior(100)
print(sys.getsizeof(warrior1.health)) #28/24 bytes for an obj in python 
