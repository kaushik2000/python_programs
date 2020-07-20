"""
Open the file mbox-short.txt and read it line by line. 
When you find a line that starts with 'From ' like the following line:

"From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

You will parse the From line using split() and print out the second word in the line 
(i.e. the entire address of the person who sent the message).
Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
"""

count = 0 # Declaring the count variable
file_handle = open("mbox-short.txt", "r") # Opening the required file 

# Splitting the filee line-by-line and then word-by-word
for line in file_handle :
    line = line.rstrip()
    if not line.startswith('From ') : continue # Ignoring/Skipping line that doesn't starts with 'From '
    words = line.split()
    print(words[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")