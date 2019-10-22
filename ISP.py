class IRect:
    def DrawRect(self):
        pass

class IShape:
    def DrawShape(self):
        pass

class Rect(IRect):
    def DrawRect(self):
        return "Rect"

class Shape(IShape):
    def DrawShape(self):
        return "Shape"