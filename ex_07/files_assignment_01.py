# Write a program that prompts for a file name,
# then opens that file and reads through the file, 
# and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.

# You can download the sample data at http://www.py4e.com/code3/words.txt

# Prompting user for the file-name
file_name = input("Enter the file name: ")
# Opening the file and reading through the file
try :
    file_handle = open(file_name, 'r')
except :
    print("File cannot be opened:", file_name)
    quit()
# Converting and printing tehe contents in UPPER CASE
for line in file_handle :
    line = line.rstrip().upper()
    print(line)