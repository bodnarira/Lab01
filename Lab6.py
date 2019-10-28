class Shape:
  def Area(self):
    pass

class Triangle(Shape):
  def __init__ (self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
  def Area (self):
    s = (self.a+self.b+self.c)/2
    return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5

class Square(Shape):
  def __init__ (self, a):
    self.a = a
  def Area (self):
    return self.a**2

class Circle(Shape):
  def __init__ (self, r):
    self.r = r
  def Area (self):
    return 3.14*self.r**2

class View ():
  def __init__ (self, shape:Shape):
    self.shape = shape
  def GetArea (self):
    return self.shape.Area()

if __name__ == "__main__":
  triangle = Triangle(2,3,4)
  square = Square(2)
  circle = Circle(3)

  viewT = View(triangle)
  viewS = View(square)
  viewC = View(circle)

  print("Triangle: " + str(viewT.GetArea()))
  print("Square: " + str(viewS.GetArea()))
  print("Circle: " + str(viewC.GetArea()))