class ILength:
    def Length (self):
        pass

class Segment(ILength):
    def __init__ (self, x1, x2):
        self.x1 = x1
        self.x2 = x2
    def Length(self):
        return self.x2-self.x1

class Circle(ILength):
    def __init__(self, radius):
        self.radius = radius
    def Length(self):
        return 2*3.14*self.radius