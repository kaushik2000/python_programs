# Using urllib library, we can do all the work that sockets do
import urllib.request, urllib.parse, urllib.error

file_handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

count = dict()
for line in file_handle :
        line = line.decode().rstrip()
        print(line)
        words = line.split()
        # print(words)
        for word in words :
                count[word] = count.get(word, 0) + 1
        
print(count)