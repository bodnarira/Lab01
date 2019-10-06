def AddTag (tagName):
    def Wrap (function):
        def inside (arg):
            t = "<" + tagName + ">"
            t2 = "</" + tagName + ">"
            return t + function(arg) + t2
        return inside
    return Wrap


@AddTag("span")
def Function3 (txt):
    return txt

print(Function3("Text"))