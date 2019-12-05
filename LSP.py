class Animal:
    def legs(self):
        pass

class Lien(Animal):
    def legs(self):
        return 4

class Monkey(Animal):
    def legs(self):
        return 2

def GetLegs (animal: Animal):
    animal.legs()
