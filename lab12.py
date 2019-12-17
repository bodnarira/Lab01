import os
import hashlib
import threading
import math


thread_n = 20
dir = "C:/Users/webvi/OneDrive/Documents/GitHub/"
duplicates = {}
files_list = []
for d in os.walk(dir):
    for i in d[2]:
        files_list.append(d[0]+"/"+i)

files_shift = math.ceil(len(files_list)/thread_n)
files_start = -files_shift
threads = []

def get_duplicates (files_start, files_end, chunk_size):
    for i in range(files_start, files_end):
        hasher = hashlib.md5()
        with open(files_list[i], 'rb') as file:
            buf = file.read(chunk_size)
        while len(buf) > 0:
            hasher.update(buf)
            buf = file.read(chunk_size)
        file.close()
        data = hasher.hexdigest()
        if data in duplicates:
            duplicates[data].append(files_list[i])
        else:
            duplicates[data] = [files_list[i]]

while True:
    files_start += files_shift
    files_end = files_start+files_shift
    if files_end > len(files_list): 
        files_end = len(files_list)
    t = threading.Thread(target=get_duplicates, args=[files_start, files_end, 65536])
    t.start()
    threads.append(t)
    if files_end == len(files_list):
        break

for t in threads:
    t.join()

for key in duplicates:
  if len(duplicates[key]) > 1:
    print(duplicates[key])