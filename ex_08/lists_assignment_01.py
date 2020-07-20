"""
Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method. 
The program should build a list of words.
For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.

You can download the sample data at http://www.py4e.com/code3/romeo.txt
"""

word_list = list() # Declaring a list() for the final word collection 
file_handle = open("romeo.txt", "r") # Opening the required file 

# Splitting the filee line-by-line and then word-by-word
for line in file_handle :
    line = line.rstrip()
    words = line.split()
    for word in words :
        if word in word_list : continue # Check if the word is already in the list
        word_list.append(word) # Appending the non-existing words
    
word_list.sort()
print(word_list)