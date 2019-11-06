class Shape:
  def area(self):
    pass

class Triangle(Shape):
  def __init__ (self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
  def area (self):
    s = (self.a+self.b+self.c)/2
    return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5

class Square(Shape):
  def __init__ (self, a):
    self.a = a
  def area (self):
    return self.a**2

class Circle(Shape):
  def __init__ (self, r):
    self.r = r
  def area (self):
    return 3.14*self.r**2

class View:
  def __init__ (self, shape:Shape):
    self.shape = shape
  def get_area (self):
    return self.shape.area()

if __name__ == "__main__":
  triangle = Triangle(2,3,4)
  square = Square(2)
  circle = Circle(3)

  view_t = View(triangle)
  view_s = View(square)
  view_t = View(circle)

  print("Triangle: " + str(view_t.get_area()))
  print("Square: " + str(view_s.get_area()))
  print("Circle: " + str(view_c.get_area()))
