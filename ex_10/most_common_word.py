# To find the most 'n' common words from a file

fname = input("Enter the file name: ")
try:
    fhand = open(fname, 'r')
except:
    print('File cannot be opened:', fname)
    quit()

# Counting the number of words in the file
counts = dict()
for line in fhand :
    line = line.rstrip()
    words = line.split() # Converting each line into a list of words
    for word in words :
        counts[word] = counts.get(word, 0) + 1
print(counts)

# Storing the dictionary as a 'value-key tuple' in a list
lst = list()
for (word, count) in counts.items() :
    new_tup = (count, word)
    lst.append(new_tup)
print("Before sorting:", lst) # Shorter verion lines 20-24 : "lst = [ (v, k) for (k,v) in counts.items() ]"

lst = sorted(lst, reverse = True) # Descending order
print("After sorting:", lst)
for (count, word) in lst[0:10] : # Getting the most 10 common words (n = 10)
    print(count, word)