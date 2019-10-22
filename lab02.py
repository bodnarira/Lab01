import html

def Decorator (d):
    def decorator(i, j = True):
        print("The old text: " + i)
        if (j):
            i = html.escape(i)
        else:
            i = html.unescape(i)

        d(i, j)
    return decorator

@Decorator
def Lab2 (i, j = True): # j - true: escape; false: unescape
    print(i)

v = '&lt;body&gt;'
b = '&<"html">'
Lab2(v, False)
Lab2(b)