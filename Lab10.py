from threading import Thread
import urllib.request
import time

class FileByUrl(Thread):
    def __init__ (self, name:str, url:str):
        Thread.__init__(self)
        self.url = url
        self.name = name

    def download (self):
        print(str(self.name)+" is downloading.")
        urllib.request.urlretrieve(self.url, self.name)
        print(str(self.name)+" downloaded")

    def run (self):
        self.download()

if __name__ == '__main__':
    files = [FileByUrl("first.jpg", "https://image.freepik.com/free-photo/wall-wallpaper-concrete-colored-painted-textured-concept_53876-31799.jpg"), 
             FileByUrl("second.jpg", "https://thumb9.shutterstock.com/thumb_large/2121473/293983418/stock-photo-paper-texture-background-293983418.jpg"),
             FileByUrl("third.jpg", "https://img.freepik.com/free-photo/dawn-hwangmasan-mountain-with-sea-clouds_127212-6.jpg?size=626&ext=jpg")]

    for file in files:
        file.start()

    for file in files:
        file.join()