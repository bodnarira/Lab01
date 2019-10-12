def Decorator (function):
  @RetFunction(function)
  def Decorating (*args, **kwargs):
    return function(*args, **kwargs)
  return Decorating

def RetFunction (main_function):
  def Decorator (function):
    function.__name__ = main_function.__name__
    function.__doc__ = main_function.__doc__
    return function
  return Decorator

@Decorator
def Add (a, b):
  """A + B"""
  return a+b

print(Add.__name__)
print(Add.__doc__)