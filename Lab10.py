from urllib.request import *
import threading

def download_file (file:str, name:str, n:int):
    file_info = urlopen(Request(file)).info()
    size = int(file_info['Content-Length'])
    new_file = open(name, "w")
    new_file.write("\0"*size)
    new_file.close()
    parts = [0]
    for i in range(n-1): parts.append(parts[len(parts)-1]+int(size/n))
    parts.append(parts[len(parts)-1]+size-int(size/n)*(n-1))
    threades = []
    for i in range(1, len(parts)):
        thread = threading.Thread(target=get_part, args=[file, name, parts[i-1], parts[i]])
        thread.start()
        threades.append(thread)

    for t in threades:
        t.join()

    print("Done.")

def get_part (file:str, name:str, start:int, end:int):
    request = Request(file)
    request.add_header('Range', 'bytes='+str(start)+'-'+str(end))
    res = urlopen(request).read()
    new_file = open(name, "rb+")
    new_file.seek(start,0)
    new_file.write(bytearray(res))
    new_file.close()

if __name__ == "__main__":
    download_file("https://static.addtoany.com/images/dracaena-cinnabari.jpg", "yee.jpg", 10)
