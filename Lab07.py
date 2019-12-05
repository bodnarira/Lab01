import re
import urllib.request

class File:
  def __init__ (self, url):
    self.data = urllib.request.urlopen(url).read().decode("utf-8")
 

class Counter:
  def __init__ (self, file:File):
    self.file = file
  def WordsCount (self):
    data = self.file.data.replace("\'", "").lower()
    words = re.findall('\w+', data)
    res = {}
    for i in words:
      try: res[i] += 1
      except: res[i] = 1
    return res

if __name__ == "__main__":
  f = File("https://www.w3.org/TR/PNG/iso_8859-1.txt")
  counter = Counter(f)
  print(counter.WordsCount())
