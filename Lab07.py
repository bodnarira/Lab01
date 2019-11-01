import urllib.request

class File:
  def __init__ (self, url):
    self.data = urllib.request.urlopen(url).read().decode("utf-8")
 

class Counter:
  def __init__ (self, file:File):
    self.file = file
  def WordCount (self, word):
    return len(self.file.data.split(word))-1

if __name__ == "__main__":
  f = File("https://www.w3.org/TR/PNG/iso_8859-1.txt")
  counter = Counter(f)
  print(counter.WordCount("VULGAR"))  