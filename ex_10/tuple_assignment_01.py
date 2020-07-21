"""
Write a program to read through the mbox-short.txt 
and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time 
and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour.
"""
fname = input("Enter file name: ")
try :
    fhand = open(fname, 'r')
except :
    print("File cannot be opened:", fname)
    quit()

counts = dict()
for line in fhand :
    if not line.startswith("From ") : continue # Ignoring lines that don't start with 'From '
    line = line.rstrip()
    # Picking out the hour from the time, which is taken from the word list
    words = line.split()
    word = words[5]
    time = word.split(":") 
    hour = time[0]
    # Counts for each hour
    counts[hour] = counts.get(hour, 0) + 1

# Sorted list of tuples
lst = sorted( [(hour, count) for (hour,count) in counts.items()] )
for (hour, count) in lst :
    print(hour, count)